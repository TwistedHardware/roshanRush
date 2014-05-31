from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
#
from api.views import ProcessAPI
from GUI.views import GetPage, UserControl, DoctorView, GetImage


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'roshanRush.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/(?P<api_name>[1-9a-zA-Z,_]+)/', ProcessAPI.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'^user/$', UserControl.as_view()),
    url(r'^dicomimage/$', GetImage.as_view()),
    url(r'^doctorview/$', DoctorView.as_view()),
    url(r'$', GetPage.as_view()),
)
