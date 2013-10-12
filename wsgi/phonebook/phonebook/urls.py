from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from fonebuk.models import Contact



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.site.register(Contact)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'phonebook.views.home', name='home'),
    url(r'^/$','fonebuk.views.contacts'),
	url(r'^/add/$','fonebuk.views.add_contact'),
	url(r'^/search/$','fonebuk.views.search'),
	url(r'/star/$','fonebuk.views.starred_contacts'),
	url(r'^/(?P<contact_id>\d*)/$','fonebuk.views.delete_contact'),
    url(r'^/contactsapi$','fonebuk.views.contactsapi'),
	url(r'^/edit/(?P<contact_id>\d*)/$','fonebuk.views.edit_contact'),
	url(r'^/fav/(?P<contact_id>\d*)/$','fonebuk.views.star_mark'),
	


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
