import django
from .views import purge

if django.VERSION >= (3, 1):
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

urlpatterns = [re_path(r"^$", purge, name="purge")]
