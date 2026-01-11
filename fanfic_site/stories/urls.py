from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stories-home'),
    path('about/',views.about, name='stories-about'),
]