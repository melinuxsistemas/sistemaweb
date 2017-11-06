from modules.core.config import MainMenu as main_menu, verify_permission
from django import template
register = template.Library()


class UserPermissions:

    def can_view_permissions(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 3)

    def can_insert_permissions(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 3)

    def can_update_permissions(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 3)