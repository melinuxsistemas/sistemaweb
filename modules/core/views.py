import requests
from django.http import HttpResponse
from django.conf import settings
from django.http.response import Http404
import json

def working(request):
    if request.is_ajax():
        request_page = request.GET['request_page']
        working_key = get_working_key()
        data = post_request(request_page,working_key)
        data = json.dumps(data)
        print("RESPONSE: ",data)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404


def post_request(request_page,working_key):
    headers = {'content-type': 'application/json'}
    url = 'http://127.0.0.1:8010/api/work/register'
    data = {"request_page":request_page, "working_key":working_key}
    response = requests.get(url, data, headers=headers)
    return response.json()#json.loads(response.text)['msg'])

def get_working_key():
    config = json.loads(open(settings.WORKING_CONFIGURATION).read())
    if config:
        working_key = config['project_key'] + "&" + config['user_key'] + "&" + config['task']
    else:
        working_key = None
    return working_key