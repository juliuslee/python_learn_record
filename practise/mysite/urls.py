from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    # Examples:
    #(r'^$', 'mysite.views.home', name='home'),
    #(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
	(r'^hello/$', 'hello'),
	(r'^time/$', 'current_datetime'),
	(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
	(r'^display_meta/$', 'display_meta'),
	(r'^current/', 'ua_display'),
	(r'^shuangseqiu/$', 'shuangseqiu'),
)

urlpatterns += patterns('books.views',
	(r'^search-form/$', 'search_form'),
	(r'^search/$', 'search'),
)

urlpatterns += patterns('contact.views',
	(r'^contact/$', 'contact'),
	(r'^contact/thanks/$', 'thanks'),
)

urlpatterns += patterns('temp.views',
	(r'^foo/$', 'foobar_view', {'template_name': 'template1.html'}),
	(r'^bar/$', 'foobar_view', {'template_name': 'template2.html'}),
)
