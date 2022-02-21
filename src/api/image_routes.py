import logging
from http import HTTPStatus

from flask import Blueprint, request, send_file

from .errors import BadRequest, NotFound
from image_worker.image_jobs import create_resize_job, get_job_result

image_bp = Blueprint('image_bp', __name__)
logger = logging.getLogger()


@image_bp.route('/resize', methods=['POST'])
def resize():
    image = request.files.get('image')
    if not image:
        raise BadRequest('Missing image file')

    job_id = create_resize_job(image.read())
    return {'job_id': job_id}, HTTPStatus.CREATED


@image_bp.route('/resize/<job_id>', methods=['GET'])
def get_image(job_id: str):
    result = get_job_result(job_id)
    if not result:
        raise NotFound('Job not found')
    if isinstance(result, str):
        return result, HTTPStatus.ACCEPTED
    return send_file(result,  mimetype='image/jpg')
