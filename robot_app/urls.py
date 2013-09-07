from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^RoMIE/admin/', include(admin.site.urls)), 
    url(r'^RoMIE/', include('robot_control.urls')),
    url(r'^/', include('robot_control.urls')),
    #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/ico/favicon.ico'}),

)
