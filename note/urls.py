from django.conf.urls import url

from note.views import note

urlpatterns = [
    url(r'^$', note, name='note'),
    # url(r'^about/$', about, name='about'),
]
