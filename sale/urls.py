"""sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.utils.functional import curry

from cars import views


from cars.views import cars_list, car_detail, services_list, service_detail
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import server_error, page_not_found, permission_denied


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', cars_list, name='home'),
    url(r'^(?P<car_id>\d+)/$', car_detail, name='car'),
    url(r'^service$', services_list, name='service-home'),
    url(r'^service(?P<service_id>\d+)/$', service_detail, name='service'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
