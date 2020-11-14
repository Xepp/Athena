from flask_script import Command
from flask_script import Option
from gunicorn.app.base import Application


class FlaskApplication(Application):

    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {
            key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


class GunicornCommand(Command):

    def __init__(self, app, host='127.0.0.1', port=5000, workers=4):
        self.app = app
        self.host = host
        self.port = port
        self.workers = workers

    def get_options(self):
        return [
            Option('-h', '--host', dest='host', default=self.host),
            Option('-p', '--port', dest='port', default=self.port),
            Option('-w', '--workers', dest='workers', default=self.workers)
        ]

    def run(self, host, port, workers):
        options = {
            'bind': f'{host}:{port}',
            'workers': workers
        }

        FlaskApplication(self.app, options).run()

