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

    # Create view tests
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

    # delete view tests
    def test_only_owner_can_delete_favorite(self):
        # user is the malicious one in this test not alice
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("favorites:delete", args=[self.alice_favorite.id]),
        )
        self.assertEquals(response.status_code, 403)
        self.assertEquals(Favorite.objects.count(), 1)

    def test_favorite_delete_view_get(self):
        self.client.force_login(self.alice)
        response = self.client.get(
            reverse("favorites:delete", args=[str(self.alice_favorite.id)])
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "favorites/partials/delete.html")

    def test_favorite_delete_view_post(self):
        self.client.force_login(self.alice)
        response = self.client.post(
            reverse("favorites:delete", args=[self.alice_favorite.id])
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Favorite.objects.count(), 0)
