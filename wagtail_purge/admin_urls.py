from .views import purge

from django.urls import re_path

urlpatterns = [re_path(r"^$", purge, name="purge")]
