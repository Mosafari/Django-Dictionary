from django.urls import path
from . import views

urlpatterns = [
    # adding home path
    path('home/', views.home, name='home'),
]
