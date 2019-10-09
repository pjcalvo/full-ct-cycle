class ApiBase:

    def __init__(self, context):
        self.context = context

    @property
    def url(self):
        return self.context.config.userdata.get('base_api_url')