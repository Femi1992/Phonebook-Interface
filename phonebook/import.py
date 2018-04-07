import requests
import sys, os

project_dir = "/Users/femi/PycharmProjects/phonebook_interface/phonebook/phonebook"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from contact.models import Contact
url = "http://www.mocky.io/v2/581335f71000004204abaf83"

contact_list = requests.get(url).json()

for items in contact_list:
    for x in contact_list[items]:
        contact = Contact()
        contact.name = x['name']
        contact.phone_number = x['phone_number']
        contact.address = x['address']
        contact.save()
