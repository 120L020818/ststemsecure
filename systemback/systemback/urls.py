"""systemback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from . import test_controller

urlpatterns = [
    url(r'api/test', test_controller.controller_test),
    url(r'api/vd1', test_controller.controller_download1),
    url(r'api/ud2', test_controller.controller_download2),
    url(r'api/first', test_controller.controller_first),
    url(r'api/second', test_controller.controller_second),
    url(r'api/dele', test_controller.controller_delete),
    url(r'api/update', test_controller.controller_update),
    url(r'api/233', test_controller.controller_233),
    url(r'api/email', test_controller.controller_email),
    url(r'api/username', test_controller.controller_username),
    url(r'api/getusername', test_controller.controller_getusername),
    url(r'api/kill', test_controller.controller_kill),
    url(r'api/knowkill', test_controller.controller_knowkill),
    # url(r'api/period', test_controller.controller_period),
]
