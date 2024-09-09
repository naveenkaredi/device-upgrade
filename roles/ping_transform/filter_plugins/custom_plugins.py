class FilterModule(object):
    def filters(self):
        return {
            'transform': self.transform,
        }

    def transform(self, data):
        res = {}
        for item in data:
            if item['destination'] not in res:
                res[item['destination']] = {}
            res[item['destination']][item['source']] = item['value']
        return res
                
                           