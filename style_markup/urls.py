from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import Home

urlpatterns = patterns('',
    
    url(r'^$', Home.as_view(), name='home'),
    url(r'^t/', include('style_markup.transformer.urls')),

    # url(r'^_ad/', include(admin.site.urls)),
)
