from flask import render_template
from flask.views import View
from urllib2 import urlopen
from erv import utils

import json


class ElectionResults(View):
    methods = ['GET']

    def dispatch_request(self, year, type_slug, commune_slug):
        '''Get the ElectionResults from the given year,
         and election type, and the commune.
         :param year: the given year of the election
         :param type_slug: the given type of election
         :param commune_slug: the given commune
        '''
        results = self.get_election_results(year, type_slug, commune_slug)

        return render_template(
            'results.html',
            election_results=results)

    def get_election_results(self, year, type_slug, commune_slug):
        '''
        '''
        api_url = utils.get_api_url()

        request_url = "%s/%i/%s/%s" % (api_url, year, type_slug, commune_slug)

        response = urlopen(request_url).read()

        election_results = json.loads(response)

        return election_results
