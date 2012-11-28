# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.servers.basehttp import FileWrapper
import simplejson as json
from django.core.urlresolvers import reverse


import re
from dbapp.models import Device
from dbapp.models import OVS
from dbapp.models import Connection
from dbapp.models import Topology
from django.db import connection
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def device_create(request,top_id):
        res=HttpResponse()
        dname=request.REQUEST["name"]
        dpos=request.REQUEST["pos"]
        p=Device(name=dname,pos=dpos,topology_id=top_id)
        p.save()
        res.write(str(p.id))
        return res
@csrf_exempt
def device_load(request,top_id):
        #res=HttpResponse()
        #res['Content-Type']="text/html"
        p=Device.objects.filter(topology=top_id)
	q=OVS.objects.filter(topology=top_id)
	c=Connection.objects.filter(topology=top_id)
        #html="hehe"
        #for i in p:
        #        html+="<div id="+str(i.id)+" class=drag style='position:absolute;"+i.pos+"'><img src='/static/jsui2/images/kvm.png'/>"+i.name+"</div>"
        #res.write(html)
        return render_to_response("top/devices.html",{"dev_list":p,"ovs_list":q,"con_list":c,"top_id":top_id})
@csrf_exempt
def device_remove(request,dev_id):
	p=Device.objects.get(id=dev_id)
	p.delete()
	return HttpResponse()
@csrf_exempt
def ovs_create(request,top_id):
        res=HttpResponse()
        oname=request.REQUEST["name"]
        opos=request.REQUEST["pos"]
        p=OVS(name=oname,pos=opos,topology_id=top_id)
        p.save()
        res.write(str(p.id))
        return res
@csrf_exempt
def ovs_remove(request,dev_id):
        p=OVS.objects.get(id=dev_id)
        p.delete()
        return HttpResponse()
@csrf_exempt
def top_tab(request,top_id):
        p=Topology.objects.get(id=top_id)
        return render_to_response("top/top_tab.html",{"top":p})
@csrf_exempt
def top_mod(request,top_id):
        p=Topology.objects.get(id=top_id)
        p.name=request.REQUEST["name"]
        p.save()
        return HttpResponse()
@csrf_exempt
def ovs_tab(request,dev_id):
	p=OVS.objects.get(id=dev_id)
	return render_to_response("top/ovs_tab.html",{"ovs":p})
@csrf_exempt
def ovs_mod(request,dev_id):
	p=OVS.objects.get(id=dev_id)
	p.name=request.REQUEST["name"]
	p.dtype=request.REQUEST["type"]
	p.save()
	return HttpResponse()
@csrf_exempt
def host_tab(request,dev_id):
        p=Device.objects.get(id=dev_id)
        return render_to_response("top/host_tab.html",{"host":p})
@csrf_exempt
def host_mod(request,dev_id):
        p=Device.objects.get(id=dev_id)
        p.name=request.REQUEST["name"]
        p.dtype=request.REQUEST["type"]
        p.save()
        return HttpResponse()
@csrf_exempt
def con_create(request,top_id):
	csource=request.REQUEST["source"]
	ctarget=request.REQUEST["target"]
	p=Connection(source=csource,target=ctarget,topology_id=top_id)
	p.save()
	return HttpResponse()
@csrf_exempt
def con_remove(request,top_id):
        csource=request.REQUEST["source"]
        ctarget=request.REQUEST["target"]
	p=Connection.objects.filter(source=csource,target=ctarget)
	p.delete()
	return HttpResponse()
@csrf_exempt
def con_tab(request):
	csource=request.REQUEST["source"]
	ctarget=request.REQUEST["target"]
	p=Connection.objects.get(source=csource,target=ctarget)
	if csource[:3]=="hst":
		s=Device.objects.get(id=csource[3:])
	else:
		s=OVS.objects.get(id=csource[3:])
	if ctarget[:3]=="hst":
		t=Device.objects.get(id=ctarget[3:])
	else:
		t=OVS.objects.get(id=ctarget[3:])
        return render_to_response("top/con_tab.html",{"con":p,"source":s,"target":t})
@csrf_exempt
def con_mod(request,s_id,t_id):
        p=Connection.objects.get(source=s_id,target=t_id)
        p.sourceport=request.REQUEST["sourceport"]
        p.targetport=request.REQUEST["targetport"]
	p.bandwidth=request.REQUEST["bandwidth"]
	p.save()
        return HttpResponse()

def run(request,top_id):
	#channel=rabbitmqConnector.RabbitmqConnector()
	#channel.exchangeDeclare('backend', 'direct')
	#channel.exchangeDeclare('frontend', 'direct')
	#channel.publish('frontend', 'config', "hehe")
	return HttpResponse()
