from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from lighthouse.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lighthouse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'lighthouse.views.start_page'),
    
)
