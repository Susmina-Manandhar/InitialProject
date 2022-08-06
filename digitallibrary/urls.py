from .views import response
from django.urls import path
urlpatterns = [
    path("digitalLibrary/",response,name="Response"),
]
