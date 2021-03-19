from wagtail.core import hooks
from wagtail.admin.menu import AdminOnlyMenuItem
from django.urls import include, reverse, path
from . import admin_urls


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path(r"purge/", include(admin_urls)),
    ]


@hooks.register("register_settings_menu_item")
def register_purge_menu_item():
    return AdminOnlyMenuItem(
        "CDN purge",
        reverse("purge"),
        classnames="icon icon-collapse-down",
        order=1000,
    )