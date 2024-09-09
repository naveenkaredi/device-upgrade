class FilterModule(object):
    def filters(self):
        return {
            'get_rsync_server': self.get_rsync_server,
        }

    def get_rsync_server(self, data):
        rsync_server = ""
        mn_value = 10000000
        print("TESETADSF")
        print(data)
        for server, value in data.items():
            if value < mn_value:
                value = mn_value
                rsync_server = server
        return rsync_server
