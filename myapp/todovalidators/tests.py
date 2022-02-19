from django.test import TestCase
from .models import todo

class TodoTestCase(TestCase):
    def create_item(self):
        data = {
            "title": "akhil"
        }
        todo.objects.create(**data)

    def setUp(self) -> None:
        self.create_item()

    def test_draft_items(self):
        qs = todo.objects.filter(publish_status=todo.PublishCoice.PUBLISHED)
        self.assertTrue(qs.exists())
