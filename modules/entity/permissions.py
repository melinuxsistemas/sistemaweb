from modules.core.config import MainMenu as main_menu, verify_permission
from django import template
register = template.Library()


class EntityPermission:
    def can_view_entity(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 1)

    def can_insert_entity(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 4)

    def can_update_entity(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 2)

    def can_disable_entity(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 3)


class ContactPermission:

    def can_access_contact(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 0)

    def can_view_contact(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 1)

    def can_insert_contact(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 2)

    def can_update_contact(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 2)

    def can_disable_contact(self):
        return verify_permission(self.user.permissions.registration[main_menu.registration.entities.id], 3)