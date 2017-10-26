from conf.user import setup


class WorkingConfig:
    working_server = "http://127.0.0.1:8010"
    working_register = working_server + "/api/work/register"
    working_status = setup.working_paramters

class UserConfigurations:
    WORKING = WorkingConfig