from django.test import TestCase
from .models import (
    Item,
    create_item,
    get_all_items,
    search_items,
    get_item,
    update_item,
    delete_item,
)



class TestItem(TestCase):
    def test_can_create_item(self):
        item = create_item("John", "John works on the farm")

        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "John")
        self.assertEqual(item.description, "John works on the farm")

    def test_can_view_all_items_at_once(self):
        items_data = [
            {
                "name": "John",
                "description": "John works on the farm",
            },
            {
                "name": "Joe",
                "description": "Joe is a blacksmith",
            },
            {
                "name": "Jill",
                "description": "Jill works on the farm too",
            },
        ]

        for item_data in items_data:
            create_item(item_data["name"], item_data["description"])

        items = get_all_items()

        self.assertEqual(len(items), len(items_data))

        items_data = sorted(items_data, key=lambda i: i["name"])
        items = sorted(items, key=lambda i: i.name)

        for data, item in zip(items_data, items):
            self.assertEqual(data["name"], item.name)
            self.assertEqual(data["description"], item.description)

    def test_can_search_by_name(self):
        items_data = [
            {
                "name": "John",
                "description": "John works on the farm",
            },
            {
                "name": "Joe",
                "description": "Joe is a blacksmith",
            },
            {
                "name": "Jill",
                "description": "Jill works on the farm too",
            },
        ]

        for item_data in items_data:
            create_item(item_data["name"], item_data["description"])

        self.assertEqual(len(search_items("John")), 1)
        self.assertEqual(search_items("John")[0].name, "John")

    def test_can_update_item(self):
        item = create_item("John", "John works on the farm")
        update_item(item.id, "Johnny", "Johnny works on the farm now")

        updated_item = get_item(item.id)

        self.assertEqual(updated_item.name, "Johnny")
        self.assertEqual(updated_item.description, "Johnny works on the farm now")

    def test_can_delete_item(self):
        item = create_item("John", "John works on the farm")
        delete_item(item.id)

        with self.assertRaises(Item.DoesNotExist):
            get_item(item.id)

    def test_can_get_item(self):
        item = create_item("John", "John works on the farm")
        fetched_item = get_item(item.id)
        self.assertEqual(fetched_item.name, "John")
        self.assertEqual(fetched_item.description, "John works on the farm")
