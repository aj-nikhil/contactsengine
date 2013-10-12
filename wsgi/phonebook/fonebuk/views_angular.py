# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse	
from fonebuk.models import Contact, ContactForm
from django.db.models import Q
from django.contrib import messages

def contacts(request):
    contacts_list = Contact.objects.all()
    return render_to_response('phonebook.html', {})
	
def contactsapi(request):
    from django.core import serializers
    data = serializers.serialize('json', Contact.objects.all())
    return HttpResponse(data, content_type="application/json")

def add_contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            form.save_m2m()
            messages.success(request, 'New Contact added.')
            return redirect(reverse('/phonebook/'), {"messages":messages})
        else:
            messages.error(request, 'Form did not pass validation!')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'contact.html', context)
	
	
	
def search(request):
    query = request.GET.get('q', '')
    if query:
		qset = (
			Q(name__icontains=query) | 
			Q(email__icontains=query) | 
			Q(phone_number__icontains=query) 
			)
		results = Contact.objects.filter(qset).distinct()
    else:
		results = []
    return render_to_response ("search.html", {"results":results,"query":query})

	
def starred_contacts(request):
	contacts_list = Contact.objects.filter(is_starred=True)
	return render_to_response('phonebook_gl	.html', {'contacts_list': contacts_list})
	
	
	
def delete_contact(request, contact_id):
    contacts_list = Contact.objects.all()
    contact = Contact.objects.filter(id=contact_id)
    contact.delete()
    messages.success(request, 'Contact successfully deleted.')
    return TemplateResponse(request, 'phonebook.html', {'contacts_list': contacts_list})
	

























	

		
	