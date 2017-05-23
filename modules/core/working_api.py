from django.conf import settings
from django.http import HttpResponse
import requests
import json


class WorkingApi:

    setup_file = settings.WORKING_CONFIGURATION
    server_api = settings.WORKING_SERVER+"/api/work/register"
    user_key = None
    project_key = None
    working_key = None
    task_id = None

    def register_programming(self,request):
        request_page = request.GET['request_page']
        data = self.save(request_page)
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')

    def register_test(self):
        data = self.save('test')
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')

    def get_working_key(self):
        config = json.loads(open(settings.WORKING_CONFIGURATION).read())
        self.user_key = config['user_key']
        self.project_key = config['project_key']
        self.task_id = config['task']

        if config:
            self.working_key = config['project_key'] + "&" + config['user_key'] + "&" + config['task']
        else:
            self.working_key = None
        return self.working_key

    def save(self,workon):
        headers = {'content-type': 'application/json'}
        data = {"request_page": workon, "working_key": self.get_working_key()}
        response = requests.get(self.server_api, data, headers=headers)
        return response.json()  # json.loads(response.text)['msg'])
