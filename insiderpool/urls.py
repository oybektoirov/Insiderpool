from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^account/', include('account.urls')),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^beers/$', 'beer.views.BeersAll'),
    (r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer'),
    (r'^brewerys/(?P<breweryslug>.*)/$', 'beer.views.SpecificBrewery'),
    (r'^register/$', 'people.views.PeopleRegistration'),
    (r'^login/$', 'people.views.LoginRequest'),
    (r'^logout/$', 'people.views.LogoutRequest'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^profile/$', 'people.views.Profile'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
                            )
