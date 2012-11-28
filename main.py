from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('potato.pro.index'))
        else:
		return render_to_response("main/start.html")

