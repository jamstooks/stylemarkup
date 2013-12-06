from django.conf.urls import patterns, url

from views import TransformGist, GistPDF

urlpatterns = patterns(
    '',

    url(r'^(?P<markup>[^/]+)/gist/(?P<id>[^/]+)/$', TransformGist.as_view(), name="gist"),
    url(r'^(?P<markup>[^/]+)/gist/(?P<id>[^/]+)/pdf/$', GistPDF.as_view(), name="gist-pdf"),
)