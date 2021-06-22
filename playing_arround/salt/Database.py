

class Database:
    def __init__(self, path):
        self.path = path
        self.samples = self.load_samples_on_init()
        self.models = self.load_models_on_init()

    def load_samples_on_init(self):
        samples = []
        print(self.path)
        # read from path
        return samples

    def add_sample(self, sample):
        self.samples.append(sample)

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
