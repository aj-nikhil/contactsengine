# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render, redirect
from django.template.response import TemplateResponse	
from fonebuk.models import Contact, ContactForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import *

def contacts(request):
    contacts_list = Contact.objects.all()
    paginator = Paginator(contacts_list, 8) # Show 8 contacts per page
    page = request.GET.get('page',1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('phonebook_gl.html', {'contacts_list':contacts})
	
def contactsapi(request):
    query = request.GET.get('term', '')
    if query:
		qset = (
			Q(name__icontains=query) | 
			Q(email__icontains=query) | 
			Q(phone_number__icontains=query) 
			)
		results = Contact.objects.filter(qset).distinct()
    else:
		results = []
    from django.core import serializers
    data = serializers.serialize('json', results)
    return HttpResponse(data, content_type="application/json")

def add_contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            form.save_m2m()
            messages.success(request, 'New Contact added.')
            return HttpResponseRedirect('/phonebook/')
        else:
            messages.error(request, 'Form did not pass validation!')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'contact.html', context)
	
def search(request):
    query = request.GET.get('term', '')
    if query:
		qset = (
			Q(name__icontains=query) | 
			Q(email__icontains=query) | 
			Q(phone_number__icontains=query) 
			)
		results = Contact.objects.filter(qset).distinct()
    else:
		results = []
    return render_to_response ("search.html", {"contacts_list":results,"query":query})

	
def starred_contacts(request):
    contacts_list = Contact.objects.filter(is_starred=True)
    paginator = Paginator(contacts_list, 8) # Show 8 contacts per page
    page = request.GET.get('page',1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
    	contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('starred.html', {'contacts_list': contacts})
	
	
	
def delete_contact(request, contact_id):
    contact = Contact.objects.filter(id=contact_id)
    contact.delete()
    return HttpResponse('')
	
	
def edit_contact(request, contact_id=None):

    f = Contact.objects.get(id=contact_id)
    
    if f is None:
       raise Http404('a was not found')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=f)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/phonebook/')
    else:
        form = ContactForm( instance = f )
    context = {
        'form': form,
		'messages': messages,
		'f':f,
    }		
    return TemplateResponse(request, 'edit_form.html', context)
	
def star_mark(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	if contact.is_starred is False:
		contact.is_starred = True
		contact.save()
	else:
		contact.is_starred is True
		contact.save()
	return HttpResponse('')
	















	

	























	

		
	