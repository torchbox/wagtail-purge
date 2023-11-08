from django.urls import include, reverse, path
from wagtail.admin.menu import AdminOnlyMenuItem

from wagtail import hooks, VERSION as WAGTAIL_VERSION
    
from . import admin_urls

@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(r"purge/", include(admin_urls)),
    ]


@hooks.register("register_settings_menu_item")
def register_purge_menu_item():
    if WAGTAIL_VERSION >= (5, 2):
            kwargs = {"classname": "icon icon-collapse-down"}
        else:
            kwargs = {"classnames": "icon icon-collapse-down"}

    return AdminOnlyMenuItem(
        "CDN purge",
        reverse("purge"),
        order=1000,
        **kwargs
    )
