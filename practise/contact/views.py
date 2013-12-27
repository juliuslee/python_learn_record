from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from contact.forms import ContactForm
#from django.template import RequestContext

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
					cd['subject'],
					cd['message'],
					cd.get('email', 'julius.luck@gmail.com'),
					['dxx_study@163.com'],
					)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
				initial={'subject': ''}
				)
	return render_to_response('contact_form.html', {'form': form},context_instance=RequestContext(request))

def thanks(request):
	thanks = "Thanks for your suggestion !"
	return render_to_response('thanks.html', locals(),context_instance=RequestContext(request))
