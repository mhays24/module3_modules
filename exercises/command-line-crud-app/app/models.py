from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


def create_item(name, description):
    item = Item(name=name, description=description)
    item.save()
    return item


def get_all_items():
    return Item.objects.all()


def search_items(query):
    return Item.objects.filter(name__icontains=query)


def get_item(id):
    return Item.objects.get(id=id)


def update_item(id, name, description):
    item = Item.objects.get(id=id)
    item.name = name
    item.description = description
    item.save()
    return item


def delete_item(id):
    item = Item.objects.get(id=id)
    item.delete()
