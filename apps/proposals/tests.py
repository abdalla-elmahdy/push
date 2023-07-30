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

        cls.proposal = Proposal.objects.create(
            sender=cls.user,
            project=cls.project,
            motive="Lorem ipsum",
            skillset="Lorem ipsum",
            contact_details="Lorem ipsum",
        )

    # create view tests
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
        self.assertEqual(Proposal.objects.count(), 2)
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
        self.assertEqual(Proposal.objects.count(), 1)
        self.assertContains(response, "Something went wrong, try again.")

    # delete view tests
    def test_only_owner_can_delete_proposal(self):
        self.client.force_login(self.alice)
        response = self.client.post(
            reverse("proposals:delete", args=[str(self.proposal.id)])
        )
        self.assertEquals(response.status_code, 403)
        self.assertEquals(Proposal.objects.count(), 1)

    def test_proposal_delete_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("proposals:delete", args=[str(self.proposal.id)])
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "proposals/partials/delete.html")

    def test_proposal_delete_view_post(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("proposals:delete", args=[self.proposal.id])
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Proposal.objects.count(), 0)
