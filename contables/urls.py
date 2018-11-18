
from django.conf.urls import url
from django.contrib import admin

from apps.sistemacontable.views import main,index,transaccion, preTransaccion
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^index/', index),
    url(r'^transaccion/', transaccion),
    url(r'^preTransaccion/', preTransaccion),
]
