""" 
	Python library for interacting with the CRP API.

    The CRP API (http://www.opensecrets.org/action/api_doc.php) provides campaign 
	finance and other data from the Center for Responsive Politics.

	See README.rst for methods and usage
"""

__author__ = "James Turk (jturk@sunlightfoundation.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2009 Sunlight Labs"
__license__ = "BSD"

import urllib.parse
import requests
try:
    import json
except ImportError:
    import simplejson as json

class CRPApiError(Exception):
    """ Exception for CRP API errors """

# results #
class CRPApiObject(object):
    def __init__(self, d):
        self.__dict__ = d

# namespaces #

class CRP(object):

    apikey = None

    @staticmethod
    def _apicall(func, params):
        if CRP.apikey is None:
            raise CRPApiError('Missing CRP apikey')

        protocol = 'https'
        server = 'www.opensecrets.org'
        url = '%s://%s/api/?method=%s&output=json&apikey=%s&%s' % \
              (protocol, server, func, CRP.apikey, urllib.parse.urlencode(params))
        try:
            response = requests.get(url)
            return response.json()
        except requests.HTTPError as e:
            raise CRPApiError(e.read())
        except (ValueError, KeyError) as e:
            raise CRPApiError('Invalid Response')

    class getLegislators(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('getLegislators', kwargs)
            return results

    class memPFDprofile(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('memPFDprofile', kwargs)['response']['member_profile']
            return results

    class candSummary(object):
        @staticmethod
        def get(**kwargs):
            result = CRP._apicall('candSummary', kwargs)
            return result['@attributes']

    class candContrib(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candContrib', kwargs)['response']['contributors']
            return results

    class candIndustry(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candIndustry', kwargs)
            return results

    class candSector(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candSector', kwargs)
            return results

    class candIndByInd(object):
        @staticmethod
        def get(**kwargs):
            result = CRP._apicall('CandIndByInd', kwargs)
            return result['response']['candIndus']['@attributes']

    class getOrgs(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('getOrgs', kwargs)
            return results
            
    class orgSummary(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('orgSummary', kwargs)
            return results
            
    class congCmteIndus(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('congCmteIndus', kwargs)
            return results
