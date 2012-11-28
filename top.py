#Mi create this file

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from dbapp.models import Topology
from dbapp.models import Device
from dbapp.models import OVS
from dbapp.models import Connection
from django.db import connection
from django.template import RequestContext

def index(request):
#    cursor = connection.cursor()
#    cursor.execute("SELECT id,name FROM dbapp_Project")
#    an=cursor.fetchall()
    top_list=Topology.objects.all()
    return render_to_response("topology/index.html",{"top_list":top_list})

def create(request,pro_id):
    p=Topology(owner='admin',project_id=pro_id)
    p.save()
    p.name = "Topology "+str(p.id)
    p.save()
    return render_to_response("top/editor.html",{"pro_id":pro_id,"top_id":p.id,"edit":True},context_instance=RequestContext(request))

def remove(request,pro_id,top_id):
    p=Topology.objects.get(id=top_id)
    p.delete()
    return HttpResponseRedirect(reverse('potato.pro.info',kwargs={"pro_id":pro_id}))
    


def show(request,pro_id,top_id):
#    top=Topology.objects.get(id=top_id)
    return render_to_response("top/editor.html",{"pro_id":pro_id,"top_id":top_id,"edit":False},context_instance=RequestContext(request))


def edit(request,pro_id,top_id):
    return render_to_response("top/editor.html",{"pro_id":pro_id,"top_id":top_id,"edit":True},context_instance=RequestContext(request))
def export(request,pro_id,top_id):
    hst_list=Device.objects.filter(topology=top_id)
    ovs_list=OVS.objects.filter(topology=top_id)
    con_list=Connection.objects.filter(topology=top_id)
    return render_to_response("top/export.html",{"hst_list":hst_list,"ovs_list":ovs_list,"con_list":con_list})
