from django import template
from modules.core.config import MainMenu as main_menu, verify_permission

register = template.Library()

@register.inclusion_tag('core/components/option_menu.html')
def option_menu(item_name, item_url, new_option, permission):
    return {'item_name':item_name,'item_url':item_url,'new_option':new_option,'permission':permission}

