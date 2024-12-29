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


class PrivateTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        topic1 = Topic.objects.create(name="Crime")
        topic2 = Topic.objects.create(name="Business")
        Newspaper.objects.create(
            title="Crime News",
            content="Detailed report on recent crimes.",
            published_date="2025-01-01",
            topic=topic1
        )
        Newspaper.objects.create(
            title="Business News",
            content="Latest updates in the business world.",
            published_date="2025-01-01",
            topic=topic2
        )
        redactor1 = Redactor.objects.create(
            username="jdoe",
            first_name="John",
            last_name="Doe",
            years_of_experience=5
        )
        redactor2 = Redactor.objects.create(
            username="asmith",
            first_name="Alice",
            last_name="Smith",
            years_of_experience=7
        )
        redactor1.set_password("test12345")
        redactor2.set_password("test12345")
        redactor1.save()
        redactor2.save()

    def setUp(self) -> None:
        user = Redactor.objects.create(
            username="test",
            years_of_experience=4
        )
        user.set_password("test12345")
        user.save()
        self.client.force_login(user)

    def test_retrieve_topics(self) -> None:
        response = self.client.get(reverse("newspapers:topic-list"))
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "newspapers/topic_list.html")

    def test_retrieve_newspapers(self) -> None:
        response = self.client.get(reverse("newspapers:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        newspapers = Newspaper.objects.all()
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(response, "newspapers/newspaper_list.html")

    def test_retrieve_redactors(self) -> None:
        response = self.client.get(reverse("newspapers:redactor-list"))
        self.assertEqual(response.status_code, 200)
        redactors = Redactor.objects.all()
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(response, "newspapers/redactor_list.html")


class SearchTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        topic1 = Topic.objects.create(name="Crime")
        topic2 = Topic.objects.create(name="Business")
        Newspaper.objects.create(
            title="Crime News",
            content="Detailed report on recent crimes.",
            published_date="2025-01-01",
            topic=topic1
        )
        Newspaper.objects.create(
            title="Business News",
            content="Latest updates in the business world.",
            published_date="2025-01-01",
            topic=topic2
        )
        redactor1 = Redactor.objects.create(
            username="jdoe",
            first_name="John",
            last_name="Doe",
            years_of_experience=5
        )
        redactor2 = Redactor.objects.create(
            username="asmith",
            first_name="Alice",
            last_name="Smith",
            years_of_experience=7
        )
        redactor1.set_password("test12345")
        redactor2.set_password("test12345")
        redactor1.save()
        redactor2.save()

    def setUp(self) -> None:
        user = Redactor.objects.create(
            username="test",
            years_of_experience=2
        )
        user.set_password("test1245")
        user.save()
        self.client.force_login(user)

    def test_search_topic_by_name(self) -> None:
        response = self.client.get(
            reverse("newspapers:topic-list"), {"name": "Crime"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crime")
        self.assertNotContains(response, "Business")

    def test_search_redactor_by_username(self) -> None:
        response = self.client.get(
            reverse("newspapers:redactor-list"), {"username": "asmith"}
        )
        self.assertEqual(response, 200)
        self.assertContains(response, "asmith")
        self.assertNotContains(response, "jdoe")

    def test_search_newspaper_by_title(self) -> None:
        response = self.client.get(
            reverse("newspapers:newspaper-list"), {"title": "Business News"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Business News")
        self.assertNotContains(response, "Crime News")
