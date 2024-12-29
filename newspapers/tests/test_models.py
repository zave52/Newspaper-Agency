from django.test import TestCase

from newspapers.models import Redactor, Topic, Newspaper


class RedactorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        redactor = Redactor.objects.create(
            username="test",
            first_name="First name",
            last_name="Last name",
            years_of_experience=4
        )
        redactor.set_password("test12345")
        redactor.save()

    def test_get_str(self) -> None:
        redactor = Redactor.objects.get(id=1)
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_create_redactor_with_years_of_experience(self) -> None:
        redactor = Redactor.objects.get(id=1)
        self.assertEqual(redactor.username, "test")
        self.assertTrue(redactor.check_password("test12345"))
        self.assertEqual(redactor.years_of_experience, 4)


class TopicModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Topic.objects.create(name="test")

    def test_get_str(self) -> None:
        topic = Topic.objects.get(id=1)
        self.assertEqual(str(topic), topic.name)


class NewspaperModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        topic = Topic.objects.create(name="test")
        Newspaper.objects.create(
            title="test",
            content="test content",
            published_date="2025-01-01",
            topic=topic
        )

    def test_get_str(self) -> None:
        newspaper = Newspaper.objects.get(id=1)
        self.assertEqual(
            str(newspaper),f"{newspaper.title} ({newspaper.topic.name})"
        )
