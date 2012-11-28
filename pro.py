from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from dbapp.models import Project
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
#    cursor = connection.cursor()
#    cursor.execute("SELECT id,name FROM dbapp_Project")
#    an=cursor.fetchall()
    pro_list=Project.objects.all()
    top_list_list=[]
    for pro in pro_list:
        top_list=pro.topology_set.all()
	top_list_list.append(top_list)
    return render_to_response("pro/index.html",{"pro_list":pro_list,"top_list_list":top_list_list},context_instance=RequestContext(request))
@login_required
def create(request):
    return render_to_response("pro/create.html",context_instance=RequestContext(request))
@login_required
def edit(request,pro_id):
    p=Project.objects.get(id=pro_id)
    return render_to_response("pro/create.html",{"pro":p})
@csrf_exempt
def create_db(request):
    pname=request.POST['pname']
    pattrs=request.POST['pattrs']
    pstart_time=request.POST['start_time']
    pend_time=request.POST['end_time']
    p=Project(name=pname,attrs=pattrs,owner=request.user.username,start_time=pstart_time,end_time=pend_time)
    p.save()
    return HttpResponseRedirect(reverse('potato.pro.info',kwargs={"pro_id":p.id}))
@csrf_exempt
def edit_db(request,pro_id):
    p=Project.objects.get(id=pro_id)
    p.name=request.POST['pname']
    p.attrs=request.POST['pattrs']
    p.start_time=request.POST['start_time']
    p.end_time=request.POST['end_time']
    p.save()
    return HttpResponseRedirect(reverse('potato.pro.info',kwargs={"pro_id":pro_id}))
@login_required
def remove(request,pro_id):
    p=Project.objects.get(id=pro_id)
    p.delete()
    return HttpResponseRedirect(reverse('potatopro.index'))
    

@login_required
def info(request,pro_id):
    pro=Project.objects.get(id=pro_id)
    top_list=pro.topology_set.all()
    return render_to_response("pro/info.html",{"pro_id":pro_id,"pro":pro,"top_list":top_list},context_instance=RequestContext(request))


#def addtop(request,pro_id):

