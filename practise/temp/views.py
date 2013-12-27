from django.shortcuts import render_to_response, RequestContext
from mysite import * 

def foo_view(request):
	m_list = "a test! "
	return render_to_response('template1.html', {'m_list': m_list})

def bar_view(request):
	m_list = "A test! "
	return render_to_response('template2.html', {'m_list': m_list})

