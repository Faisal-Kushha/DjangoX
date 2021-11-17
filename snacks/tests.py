from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="fkushha89@hotmail.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="user1", description=1, purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "user1")

    def test_Snack_content(self):
        self.assertEqual(f"{self.snack.title}", "user1")
        self.assertEqual(f"{self.snack.description}", '1')
        self.assertEqual(str(self.snack.purchaser), "tester")

    def test_Snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "user1")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_Snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_Snack_create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "title": "Rake",
                "description": "2",
                "purchaser": self.user.pk,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Title")

    def test_Snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"title": "Updated title", "description": "3", "purchaser": self.user.pk}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_Snack_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)