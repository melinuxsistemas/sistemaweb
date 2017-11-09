from modules.core.config import MainMenu as main_menu, verify_permission
from django import template
register = template.Library()


class EntityPermissions:
    def can_view_entity(self):
        print("EH VIEW QUE EU CHEGUEI")
        return verify_permission(self.registration[main_menu.registration.entities.id], 1)

    def can_insert_entity(self):
        print("TO VINDO AQUI",verify_permission(self.registration[main_menu.registration.entities.id], 2))
        return verify_permission(self.registration[main_menu.registration.entities.id], 2)

    def can_update_entity(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 2)

    def can_disable_entity(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 3)


class ContactPermissions:
    def can_access_contact(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 0)

    def can_view_contact(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 1)

    def can_insert_contact(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 2)

    def can_update_contact(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 2)

    def can_disable_contact(self):
        return verify_permission(self.registration[main_menu.registration.entities.id], 3)