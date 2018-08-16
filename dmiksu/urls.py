from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('note.urls', namespace='note')),
]
