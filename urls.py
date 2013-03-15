# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
URL patterns for the OpenStack Dashboard.
"""

from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import horizon
from .main import images,flavors

urlpatterns = patterns('',
#    url(r'^$', 'openstack_auth.views.login'),
    url(r'^$', 'potato.main.index'),
    url(r'^auth/', include('openstack_auth.urls')),
    
    url(r'', include(horizon.urls)),
    url(r'^pro$','potato.pro.index'),
    url(r'^pro/create$','potato.pro.create'),
    url(r'^pro/create_db$','potato.pro.create_db'),
    url(r'^pro/info$','potato.pro.info'),
    url(r'^pro/(?P<pro_id>\d+)/edit$','potato.pro.edit'),
    url(r'^pro/(?P<pro_id>\d+)/edit_db$','potato.pro.edit_db'),
    url(r'^pro/remove$','potato.pro.remove'),
    url(r'^top/create$','potato.top.create'),
    (r'^top/(?P<top_id>\d+)/show$','potato.top.show'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/edit$','potato.top.edit'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/remove$','potato.top.remove'),
    (r'^(?P<pro_id>\d+)/top/(?P<top_id>\d+)/export$','potato.top.export'),
    (r'^ajax/top/(?P<top_id>\d+)/device_create$','potato.ajax.device_create'),
    (r'^ajax/top/(?P<top_id>\d+)/device_load$','potato.ajax.device_load'),
    (r'^ajax/top/(?P<dev_id>\d+)/device_remove$','potato.ajax.device_remove'),
    (r'^ajax/top/(?P<top_id>\d+)/ovs_create$','potato.ajax.ovs_create'),
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_remove$','potato.ajax.ovs_remove'),
    (r'^ajax/top/(?P<top_id>\d+)/top_tab$','potato.ajax.top_tab'),
    (r'^ajax/top/(?P<top_id>\d+)/top_mod$','potato.ajax.top_mod'),
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_tab$','potato.ajax.ovs_tab'),
    (r'^ajax/top/(?P<dev_id>\d+)/ovs_mod$','potato.ajax.ovs_mod'),
    (r'^ajax/top/(?P<dev_id>\d+)/host_tab$','potato.ajax.host_tab'),
    (r'^ajax/top/(?P<dev_id>\d+)/host_mod$','potato.ajax.host_mod'),
    (r'^ajax/top/(?P<dev_id>\d+)/server_create$','potato.ajax.server_create'),
    (r'^ajax/top/(?P<top_id>\d+)/con_create','potato.ajax.con_create'),
    (r'^ajax/top/(?P<top_id>\d+)/con_remove','potato.ajax.con_remove'),
    (r'^ajax/top/con_tab$','potato.ajax.con_tab'),
    (r'^ajax/(?P<s_id>.+)/(?P<t_id>.+)/con_mod$','potato.ajax.con_mod'),
    (r'^ajax/top/(?P<top_id>\d+)/run','potato.ajax.run'),
    (r'^help/images$','potato.main.images2'),
    (r'^help/flavors$',flavors.as_view()),

)

# Development static app and project media serving using the staticfiles app.
urlpatterns += staticfiles_urlpatterns()

# Convenience function for serving user-uploaded media during
# development. Only active if DEBUG==True and the URL prefix is a local
# path. Production media should NOT be served by Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^500/$', 'django.views.defaults.server_error')
    )
