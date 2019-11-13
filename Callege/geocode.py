from opencage.geocoder import OpenCageGeocode
from pprint import pprint
key = 'fd81876eadb7444aa27a1b6dd6b3cee4'
geocoder = OpenCageGeocode(key)
results = geocoder.reverse_geocode(44.8303087, -0.5761911)
pprint(results)
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError

try:
    results = geocoder.reverse_geocode(44.8303087, -0.5761911, language='de', no_annotation='1')
    if results and len(results):
        print(results[0]['formatted'])
except RateLimitExceededError as ex:
    print(ex)
    # Your rate limit has expired. It will reset to 2500 on 2018-10-08T00:00:00
    # Upgrade on https://opencagedata.com/pricing
    
from ipyleaflet import *
results = geocoder.geocode(u'Brussels, Belgium')
center = (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
map = Map(center=center, zoom=6)
marker = Marker(location=center, draggable=False)
map.add_layer(marker)

map