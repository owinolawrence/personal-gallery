from django.conf.urls import url
from . iport views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome')
]