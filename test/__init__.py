from modules.core.working_api import WorkingManager
from test.unit.backend.core.test_validators import *

from test.unit.backend.usuario.test_models import *
from test.unit.backend.usuario.test_views import *
from test.unit.backend.usuario.test_routes import *


WorkingManager().register_test_backend()
