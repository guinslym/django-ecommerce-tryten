from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):
    """
    I din't implement the contact form
    """
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE'
    context = locals()
    template = 'contact.html'
    return render(request, template, context)
