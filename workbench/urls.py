
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler500

urlpatterns = [
    path('admin/', admin.site.urls), 

    path('', views.index, name="index"),
]

handler500 = views.error_500