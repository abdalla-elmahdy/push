from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.projects.models import Project

from .models import Proposal

CustomUser = get_user_model()


class ProposalTest(TestCase):
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

    def test_create_proposal_view(self):
        self.client.force_login(self.user)
        data = {
            "project_id": str(self.project.id),
            "motive": "Lorem ipsum",
            "skillset": "Lorem ipsum",
            "contact_details": "Lorem ipsum",
        }
        response = self.client.post(reverse("proposals:create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Proposal.objects.count(), 1)
        self.assertContains(response, "Proposal sent successfully")

    def test_create_proposal_view_for_project_that_doesnt_exist(self):
        self.client.force_login(self.user)
        data = {
            "project_id": "12345",
            "motive": "Lorem ipsum",
            "skillset": "Lorem ipsum",
            "contact_details": "Lorem ipsum",
        }
        response = self.client.post(reverse("proposals:create"), data)
        self.assertEqual(Proposal.objects.count(), 0)
        self.assertContains(response, "Something went wrong, try again.")
