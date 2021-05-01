# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Gold_app.urls'))
]
