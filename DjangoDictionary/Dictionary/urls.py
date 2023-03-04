from django.urls import path
from . import views

urlpatterns = [
    # adding home path
    path('home/', views.home, name='home'),
    path('home/export-ex/', views.export, name='export-ex'),
]
