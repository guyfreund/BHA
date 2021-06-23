

class Database:
    def __init__(self, path):
        self.path = path
        self.models = self.load_models_on_init()

    def load_models_on_init(self):
        models = []
        print(self.path)
        # read from path
        return models

    def add_model(self, model):
        self.models.append(model)

    def get_model_by_path(self, path):
        for model in self.models:
            if model['path'] == path:
                return model

        return None
