from .views import purge

from django.urls import path

urlpatterns = [path("", purge, name="purge")]
