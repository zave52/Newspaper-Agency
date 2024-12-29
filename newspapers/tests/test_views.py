from django.test import TestCase
from django.urls import reverse

from newspapers.models import Topic, Newspaper, Redactor


class PublicTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        topic = Topic.objects.create(name="test")
        Newspaper.objects.create(
            title="test",
            content="test content",
            published_date="2025-01-01",
            topic=topic
        )
        redactor = Redactor.objects.create(
            username="test",
            first_name="first_name",
            last_name="last_name",
            years_of_experience=3
        )
        redactor.set_password("test12345")
        redactor.save()

    def test_login_required_topic(self) -> None:
        response = self.client.get(reverse("newspapers:topic-list"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("newspapers:topic-create"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("newspapers:topic-update", args=[1]))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("newspapers:topic-delete", args=[1]))
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_newspaper(self) -> None:
        response = self.client.get(reverse("newspapers:newspaper-list"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("newspapers:newspaper-create"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:newspaper-update", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:newspaper-delete", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:newspaper-detail", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_redactor(self) -> None:
        response = self.client.get(reverse("newspapers:redactor-list"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(reverse("newspapers:redactor-create"))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:redactor-update", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:redactor-delete", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(
            reverse("newspapers:redactor-detail", args=[1])
        )
        self.assertNotEqual(response.status_code, 200)
