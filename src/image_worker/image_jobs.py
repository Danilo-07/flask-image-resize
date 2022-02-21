import os
from io import BytesIO
from typing import Union

from redis import Redis
from rq import Queue

from .resize import resize_image

redis_queue = Queue(connection=Redis(host=os.getenv('REDIS_HOST')))


def create_resize_job(image: bytes) -> str:
    job = redis_queue.enqueue(resize_image, image)
    return job.id


def get_job_result(job_id: str) -> Union[str, BytesIO]:
    job = redis_queue.fetch_job(job_id)
    if job and job.get_status() == 'finished':
        return BytesIO(job.result)
    if job and job.get_status() != 'finished':
        return 'Not Ready'

