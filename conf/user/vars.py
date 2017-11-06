import project_properties


class WorkingConfig:
    working_server = "http://192.168.1.114:8010"
    working_register = working_server + "/api/work/register"
    working_status = project_properties.working_paramters

class UserConfigurations:
    WORKING = WorkingConfig