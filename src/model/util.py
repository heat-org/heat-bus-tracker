import requests
import json
import constant

class Util:

    def request_get(endpoint,parameters):
        request_url = '{0}'+ endpoint
        request_url = request_url.format(constant.URLAPI)

        response = requests.get(request_url,headers=constant.HEADERS)
        if response.status_code == 200:
            return None
        else:
            return None
    
    def request_post(endpoint,object):
        request_url = '{0}'+ endpoint
        request_url = request_url.format(constant.URLAPI)
        dataJson = json.dumps(object.__dict__)
        response = requests.post(request_url, headers=constant.HEADERS, data=dataJson,verify=False)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None