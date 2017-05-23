from modules.core.working_api import WorkingApi
from test.unit.backend.core.test_validators import *

from test.unit.backend.usuario.test_models import *
from test.unit.backend.usuario.test_views import *
from test.unit.backend.usuario.test_routes import *
import json

workin_api = WorkingApi()
response = workin_api.register_test()
if response.status_code == 200:
    response_data = json.loads(response.content.decode())
    if response_data['success'] == True:
        data = response_data['data']['date']
        user = response_data['data']['user_name']
        project = response_data['data']['project_name']
        print(data+" > WorkingApi was updated -",user,"working on",project,)
    else:
        print("WorkingApi not update!")
else:
    print("WorkingApi not Running at moment.")
