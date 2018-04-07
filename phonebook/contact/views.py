from django.shortcuts import render
# Create your views here.
from .models import Contact
from django.views.generic import ListView

class ContactsListView(ListView):
    template_name = "contact/list.html"

    def get_queryset(self):
        all_contacts = Contact.objects.all()

        return all_contacts
