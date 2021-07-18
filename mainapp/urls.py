# from django.conf.urls import url
from django.views.decorators.cache import cache_page

import mainapp.views as mainapp
from django.urls import re_path

app_name="mainapp"

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),

    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),

    re_path(r'^category/(?P<pk>\d+)/$', cache_page(3600)(mainapp.products)),

]

    