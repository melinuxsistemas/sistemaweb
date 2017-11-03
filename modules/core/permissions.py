from modules.core.config import MainMenu as main_menu, verify_permission
from django import template

from modules.entity.permissions import EntityPermission


class RegistrationPermissions:
    entities = EntityPermission()
    purchases = None


class MenuPermissions:
    registration = RegistrationPermissions()
    permissions = None
    mercadologic_group = None
    products = None
    products_relations = None
    phones = None
    complementary_tables = None


