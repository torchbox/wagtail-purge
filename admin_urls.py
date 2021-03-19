from django.conf.urls import url
from .views import purge

urlpatterns = [url(r"^$", purge, name="purge")]
