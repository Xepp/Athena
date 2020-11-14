import unittest
from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')

        return app

    def test_app_is_development(self):
        self.assertFalse(app.config.get('SECRET_KEY') == 'secret_key')
        self.assertTrue(app.config.get('DEBUG') is True)
        self.assertFalse(current_app is None)


class TestProductionConfig(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')

        return app

    def test_app_is_production(self):
        self.assertTrue(app.config.get('DEBUG') is False)


class TestTestingConfig(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')

        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config.get('SECRET_KEY') == 'secret_key')
        self.assertTrue(app.config.get('DEBUG') is True)


if __name__ == '__main__':
    unittest.main()

