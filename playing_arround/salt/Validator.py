
import Database as DB


class Validator:
    def __init__(self, database: DB):
        self.database = database

    def validate(self, sample):
        path = sample['path']
        model = self.database.get_model_by_path(path)
        if model:
            return self.is_abnormal(model, sample)
        else:
            model_based_on_sample = self.create_model_based_on_sample(sample)
            self.database.add_model(model_based_on_sample)
            # TO THINK
            return False

    @staticmethod
    def is_abnormal(model, sample):
        # TODO
        return False

    @staticmethod
    def create_model_based_on_sample(sample):
        model = {}
        # TODO
        return model
