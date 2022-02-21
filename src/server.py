import multiprocessing
import os

import gunicorn.app.base

from api.app import create_app


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    host = os.getenv('GUNICORN_HOST', '0.0.0.0')
    port = os.getenv('GUNICORN_PORT', '8080')
    workers = os.getenv('GUNICORN_WORKERS')
    server_options = {
        'bind': f'{host}:{port}',
        'workers': int(workers or number_of_workers())
    }
    flask_app = create_app()
    StandaloneApplication(flask_app, server_options).run()
