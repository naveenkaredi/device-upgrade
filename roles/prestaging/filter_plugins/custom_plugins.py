class FilterModule(object):
    def filters(self):
        return {
            'get_rsync_server': self.get_rsync_server,
        }

    def get_rsync_server(self, data):
        return "124"
