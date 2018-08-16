from django.conf.urls import url

from note.views import index, regex, git, linux

app_name = 'note'

urlpatterns = [
    url(r'^regex/$', regex, name='regex'),
    url(r'^git/$', git, name='git'),
    url(r'^linux/$', linux, name='linux'),
    url(r'^$', index, name='index'),
]
