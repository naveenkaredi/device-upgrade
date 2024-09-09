class FilterModule(object):
    def filters(self):
        return {
            'get_rsync_server': self.get_rsync_server,
        }

    def get_rsync_server(self, data):
        current_data = None
        for k, v in data.items():
            if type(v) is dict:
                current_data = v
                break
        rsync_server = ""
        mn_value = 10000000
        for server, value in current_data.items():
            if value < mn_value:
                value = mn_value
                rsync_server = server
        return rsync_server
