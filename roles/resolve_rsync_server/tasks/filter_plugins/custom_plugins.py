class FilterModule(object):
    def filters(self):
        return {
            'transform': self.transform,
        }

    def transform(self, data):
        return ["test"]