class FilterModule(object):
    def filters(self):
        return {
            'transform': self.transform,
        }

    def transform(self, data):
        res = []
        idx_mappings = {}
        return { 
            'd1': {'f': 'd'}, 
            'd2': {'f': 'h'}
        }
       
        # for idx in range(0, len(data)):
        #     item = data[idx]
        #     if item['destination'] not in idx_mappings:      
        #         current = {}
        #         current['device'] = item['destination']
        #         current['ping_values'] = []   
        #         current['ping_values'].append({item['source']: item['value']})
        #         idx_mappings[item['destination']] = idx
        #         res.append(current)
        #     else:
        #         lst_idx = idx_mappings[item['destination']]
                
                           