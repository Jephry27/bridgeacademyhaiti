"""bridgeacademy_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from bridgeweb_app import views as bridgeweb_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', bridgeweb_views.index, name = 'index'),
#     path('bridgeacademyhaiti/', include('bridgeweb_app.urls')),
# ]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', bridgeweb_views.index, name = 'index'),
    path('lan_e', bridgeweb_views.english, name = 'english'),
    path('lan_f', bridgeweb_views.french, name = 'french'),
    path('ourprogram', bridgeweb_views.ourProgram, name = 'our_program'),
    path('our_program', bridgeweb_views.curriculum, name = 'curriculum'),
)