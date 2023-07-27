from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import CustomUser

from .models import Project


class ProjectsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get("/projects/1234")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(no_response.status_code, 404)
        self.assertTemplateUsed(response, "projects/detail.html")
        self.assertContains(response, self.project.title)

    def test_project_create_view_post(self):
        self.client.force_login(self.user)
        data = {
            "title": "Test Project",
            "description": "Test project decription",
            "open_for": "CT",
            "time_estimate": "DY",
        }
        response = self.client.post(reverse("projects:create"), data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Project.objects.count(), 2)

    def test_project_create_view_post_incomplete_data(self):
        self.client.force_login(self.user)
        data = {
            "title": "Test Project",
        }
        response = self.client.post(reverse("projects:create"), data)
        # the status code is 200 because it returns the page again
        # instead of redirecting to success page
        self.assertEquals(response.status_code, 200)
        # object count should stay the same
        self.assertEquals(Project.objects.count(), 1)

    def test_project_create_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("projects:create"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "projects/create.html")
