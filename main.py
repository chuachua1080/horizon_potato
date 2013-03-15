from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from horizon import tables
from .dashboards.admin.images.tables import AdminImagesTable
from .dashboards.admin.flavors.tables import FlavorsTable

from horizon import exceptions
from openstack_dashboard import api
import urllib
import urllib2
import json




def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('potato.pro.index'))
        else:
		return HttpResponseRedirect('/auth/login/')

#def help(request):
#	return render_to_response("help.html" ,context_instance=RequestContext(request))

class images(tables.DataTableView):
    table_class = AdminImagesTable
    template_name = 'help/images.html'

    def has_more_data(self, table):
        return self._more

    def get_data(self):
        images = []
        marker = self.request.GET.get(AdminImagesTable._meta.pagination_param,
                                      None)
        try:
            images, self._more = api.image_list_detailed(self.request,
                                                         marker=marker)
        except:
            self._more = False
            msg = _('Unable to retrieve image list.')
            exceptions.handle(self.request, msg)
        return images


class flavors(tables.DataTableView):
    table_class = FlavorsTable
    template_name = 'help/images.html'

    def get_data(self):
        request = self.request
        flavors = []
        try:
            flavors = api.flavor_list(request)
        except:
            exceptions.handle(request,
                              _('Unable to retrieve flavor list.'))
        # Sort flavors by size
        flavors.sort(key=lambda f: (f.vcpus, f.ram, f.disk))
        return flavors


def images2(request):
    d=request.user.tenant_id
#    req=urllib2.Request("http://210.25.137.229:9292/v2/images")
#    req.add_header("X-Auth-Token",d)
#    res=urllib2.urlopen(req).read()


 #   data=json.loads(res)
    t=api.nova.server_vnc_console(request,"131b53dc-be69-474d-a6c2-2e5bfcd55605")
    return render_to_response("test.html",{"p":t.url})
