from django.urls import path
from .views import response

urlpatterns=[
    path('project/',response,name="project_resp"),
]