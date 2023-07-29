from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse

from apps.projects.models import Project

from .models import Favorite

CustomUser = get_user_model()


class FavoritesTests(TransactionTestCase):
    @classmethod
    def setUp(cls):
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            email="testemail@example.com",
            first_name="John",
            last_name="Doe",
            status="ST",
            bio="My bio",
            password="testpass123",
        )

        cls.project = Project.objects.create(
            title="Project Title",
            owner=cls.user,
            description="Project description",
        )

        # for tests that need more than one user
        cls.alice = CustomUser.objects.create_user(
            username="alice",
            email="alice@example.com",
            first_name="Alice",
            last_name="Malicious",
            status="PR",
            bio="My bio",
            password="testpass123",
        )

        cls.alice_favorite = Favorite.objects.create(
            owner=cls.alice,
            project=cls.project,
        )

    def test_favorite_create_view(self):
        self.client.force_login(self.user)
        data = {
            "id": str(self.project.id),
        }
        response = self.client.post(reverse("favorites:create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.count(), 2)

    def test_favorite_create_view_duplicate(self):
        self.client.force_login(self.alice)
        data = {
            "id": str(self.project.id),
        }
        response = self.client.post(reverse("favorites:create"), data)
        self.assertEqual(Favorite.objects.count(), 1)
        self.assertContains(response, "Already added to your favorites")
