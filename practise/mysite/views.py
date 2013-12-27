from django.template.loader import get_template
from django.http import HttpResponse
import datetime
#from django.template import RequestContext
from django.shortcuts import render_to_response
import random

def hello(request):
	answer = '''
	<html>
		<head>
			<tilte><font color="#ff0000">hello,world!</font></title>
			</head>
		<body>
	<h1><font color="#0080ff"><p align="center">This is just for a test !</p></font></h1>
	<font size=5>Donot be so shine!</font>
	<b><p>Can you believe me?</p></b>
	<hr><blink>"yes" or "not"</blink></hr>
	<table border=2>
	<tr><td>first
	<br>second</br>
	third
	</td></tr>
	</table>
		</body>
	</html>
	'''
	return HttpResponse(answer)

def current_datetime(request):
	current_date = datetime.datetime.now()
	today_date = datetime.date.today()
	return render_to_response('current_datetime.html', locals())
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_date': now}))
#	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		hours = int(offset)
	except ValueError:
		raise Http404()
	time = datetime.datetime.now() + datetime.timedelta(hours=hours)
	return render_to_response('hours_ahead.html', locals())
#	return render_to_response('hours_ahead.html',{'hours':offset,'time':dt})
#local() simplified it 

#	t = get_template('hours_ahead.html')
#	html = t.render(Context({'hours':offset,'time':dt}))	
#	return HttpResponse(html)

def display_meta(request):
	values = request.META.items()
	values.sort()
	return render_to_response( 'display_meta.html', {'values': values })

def ua_display(request):
	ua = request.META.get('HTTP_USER_AGENT', 'unknown')
	return HttpResponse("Your browser is %s" % ua)

def shuangseqiu(request):
	blue = [x for x in range (1,17)]
	red = [y for y in range (1,34)]
	blueball = random.choice(blue)
	redballs = []
	for n in range(1,7):
		redballs.append(red.pop(random.randint(0, (len(red)-1))))
	redballs.sort()
	return render_to_response('shuangseqiu.html', locals())
