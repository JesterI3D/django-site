from django.urls import path

from . import views
from .views import MainView

#app_name = "mainApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('more/', views.more, name='more'),
    path('mainApp/', MainView.as_view()),
    path('skills/', views.skills, name='skills')
]
