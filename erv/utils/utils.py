from flask import current_app


class Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_url():
        ''' Get Election Results API URL.
        '''
        api_url = current_app.config['API_ELECTION_RESULTS']

        return api_url
