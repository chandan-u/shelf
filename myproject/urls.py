from django.conf.urls.defaults import patterns, include, url
from app.views import home
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    # (r'^$',direct_to_template, {
    #     'template':'index.html'
    # }),
    
         
             
                            
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
   
    # app urls 
    url('^$', home.home, name='home'),       
)
