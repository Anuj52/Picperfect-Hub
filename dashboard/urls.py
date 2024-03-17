from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Route to the index view for the dashboard app
    path('', views.index, name='index'),
]
