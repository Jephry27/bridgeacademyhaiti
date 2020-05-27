from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from bridgeweb_app import views

# urlpatterns = [
#     path('', views.index, name = 'index'),
# ]

urlpatterns = i18n_patterns (
    path('index', views.index, name = 'index'),
)
