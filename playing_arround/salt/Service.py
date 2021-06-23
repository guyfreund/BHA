
from Database import Database
from Validator import Validator
from flask import Flask
import logging

app = Flask("wow")


class Service:
    def __init__(self):
        self.database = Database("path_to_db")
        self.validator = Validator(self.database)

    @app.route('/sample/<sample>')
    def handle_sample(self, sample):
        self.database.add_sample(sample)
        logging.debug(sample)
        return self.validator.validate(sample)

    @app.route('/model/<model>')
    def handle_model(self, model):
        self.database.add_model(model)
        logging.debug(model)
        return f'Added new model of path {model["path"]}'