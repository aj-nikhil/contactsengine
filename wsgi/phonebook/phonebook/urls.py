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
    url(r'^phonebook/$','fonebuk.views.contacts'),
	url(r'^phonebook/add/$','fonebuk.views.add_contact'),
	url(r'^phonebook/search/$','fonebuk.views.search'),
	url(r'^phonebook/star/$','fonebuk.views.starred_contacts'),
	url(r'^phonebook/(?P<contact_id>\d*)/$','fonebuk.views.delete_contact'),
    url(r'^phonebook/contactsapi$','fonebuk.views.contactsapi'),
	url(r'^phonebook/edit/(?P<contact_id>\d*)/$','fonebuk.views.edit_contact'),
	url(r'^phonebook/fav/(?P<contact_id>\d*)/$','fonebuk.views.star_mark'),
	


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
