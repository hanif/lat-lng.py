import urllib2
import json
import argparse


GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=true'


def lat_lng(location):
    url = GOOGLE_MAPS_API_URL.format(urllib2.quote(location))
    resp = json.load(urllib2.urlopen(url))
    
    if (resp.get('status') == 'OK'):
    	loc = resp['results'][0]['geometry']['location']
    	return loc['lat'], loc['lng']


parser = argparse.ArgumentParser(prog='lat-lng', description='Get latitude & longitude of given address/location.')
parser.add_argument('-a','--address', dest='address', help='Address or location to be geolocated', nargs=1, required=True)
args = parser.parse_args()


if (args.address):
    print(lat_lng(args.address[0]))
     