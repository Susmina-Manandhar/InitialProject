
from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path("department/",response,name="response")
]