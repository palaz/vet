__author__ = 'luca'

from django.conf.urls import patterns, url
from vet_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^home/$', views.IndexView.as_view()),
    url(r'^staff/$', views.StaffView.as_view(), name='staff'),
    url(r'^struttura/$', views.StrutturaView.as_view(), name='struttura'),
    url(r'^dove-siamo/$', views.DoveSiamoView.as_view(), name='dove-siamo'),
    url(r'^contatti/$', views.ContattiView.as_view(), name='contatti'),
    url(r'^(?P<slug>[\w\-]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<cat>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.PageView.as_view(), name='page'),

)