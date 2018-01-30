
import requests as req
import json

class Location():
    """location class has functionality to get ip,loc,lat aqi etc..."""
    def __init__(self, request):
        super(Location, self).__init__()
        self.request = request

    def get_AQI(self, location = None):
        if location == None:
            location = self.get_location()
            lat,lon = location['loc'].split(',')
        else:
            lat,lon = location.split(',')
        print('loc in inside aqi',lat,lon)
        params={
        'lat':lat,
        'lon':lon,
        'APPID':'m953d6onf11vvufmc8gmugatqb',
        }
        url ='http://api.airpollutionapi.com/1.0/aqi'
        data = req.get(url,params=params)
        print(data.url,data.text)

    def get_location(self):
        ip=self.get_client_ip()
        ip='169.149.218.89'
        user_data = 'https://ipinfo.io/{0}/json'.format(ip)
        data = json.loads(req.get(user_data).text)
        print('ip:',data['ip'],'city: ',data['city'])
        print('loc',data['loc'])
        return data

    def get_client_ip(self):
        remote_address = self.request.META.get('REMOTE_ADDR')
        # set the default value of the ip to be the REMOTE_ADDR if available
        # else None
        ip = remote_address
        # try to get the first non-proxy ip (not a private ip) from the
        # HTTP_X_FORWARDED_FOR
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            proxies = x_forwarded_for.split(',')
            # remove the private ips from the beginning
            while (len(proxies) > 0 and
                    proxies[0].startswith(PRIVATE_IPS_PREFIX)):
                proxies.pop(0)
            # take the first ip which is not a private one (of a proxy)
            if len(proxies) > 0:
                ip = proxies[0]

        return ip
        
