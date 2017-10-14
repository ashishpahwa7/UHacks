import requests


def get_sub_locality(lat,lon):


    sensor = 'true'

    base = "http://maps.googleapis.com/maps/api/geocode/json?"

    params = "latlng={lat},{lon}&sensor={sen}".format(lat=latitude,lon=longitude,sen=sensor)
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url).json()

    for  item in response['results'][0]['address_components']:
        for categ in item['types']:
            if 'sublocality' and 'sublocality_level_2' in categ:
                print(item['short_name'])




'''
latitude = 28.6884549
longitude = 77.1757503

error = True

while(error):
    try:
        get_sub_locality(latitude, longitude)
        error = False
    except:
        error = True


'''



