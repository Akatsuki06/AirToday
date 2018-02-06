
import requests as req
import json
from AirToday import credentials as cred
class Location():
    """location class has functionality to get ip,loc,lat, aqi etc..."""
    def __init__(self, request=None):
        super(Location, self).__init__()
        self.request = request

    def get_AQI(self, location = None):
        if location == None:
            location = self.get_location()
            lat,lon = location['loc'].split(',')
        else:
            lat,lon = location.split(',')
        params={
        'lat':lat,
        'lon':lon,
        'APPID':cred.AIRPOLLUTION_APPID
        }
        url = AIRPOLLUTION_APPURL
        data = req.get(url,params=params)
        return data.json

    def get_location(self):
        ip=self.get_client_ip()
        ip='169.149.218.89'
        user_data = 'https://ipinfo.io/{0}/json'.format(ip)
        data = json.loads(req.get(user_data).text)
        return data

    def get_client_ip(self):
        remote_address = self.request.META.get('REMOTE_ADDR')
        ip = remote_address
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            proxies = x_forwarded_for.split(',')
            while (len(proxies) > 0 and
                    proxies[0].startswith(PRIVATE_IPS_PREFIX)):
                proxies.pop(0)
            if len(proxies) > 0:
                ip = proxies[0]
        return ip
