from django.test import TestCase
from .models import todo


class TodoTestCase(TestCase):
    def create_item(self):
        data = {
            "title": "akhil"
        }
        todo.objects.create(**data)
        todo.objects.create(**data)
        todo.objects.create(**data)
        self.publishedCount = 3

    def create_draft_item(self):
        data = {
            "title": "akhil",
            "publish_status": todo.PublishCoice.DRAFT
        }
        todo.objects.create(**data)
        todo.objects.create(**data)
        self.draftCount = 2

    def setUp(self) -> None:
        self.create_item()
        self.create_draft_item()

    def test_published_sample(self):
        qs = todo.objects.filter(publish_status=todo.PublishCoice.PUBLISHED)
        self.assertTrue(qs.exists())

    def test_published_items(self):
        qs = todo.objects.filter(publish_status=todo.PublishCoice.PUBLISHED)
        self.assertEqual(qs.count(), self.publishedCount)

    def test_draft_items(self):
        qs = todo.objects.filter(publish_status=todo.PublishCoice.DRAFT)
        self.assertEqual(qs.count(), self.draftCount)
