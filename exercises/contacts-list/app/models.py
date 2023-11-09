from django.db import models


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField(default=False)


def create_contact(name, email, phone, is_favorite=False) -> Contact:
    contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    contact.save()
    return contact

def all_contacts() -> list:
    return Contact.objects.all()

def find_contact_by_name(name) -> Contact:
    try:
        return Contact.objects.get(name=name)
    except: 
        return None

def favorite_contacts() -> list:
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email) -> Contact:
    contact = Contact.objects.get(name=name)
    contact.email = new_email
    contact.save()
    return contact

def delete_contact(name) -> Contact:
    contact = Contact.objects.get(name=name)
    contact.delete()
    return contact