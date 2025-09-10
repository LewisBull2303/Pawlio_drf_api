# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal:
from posts.models import Post
from saves.models import Save

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SaveTests(APITestCase):
    def setUp(self):
        """
        Create two users and one post for testing.
        """
        self.user1 = User.objects.create_user(username="Lewis", password="password")
        self.user2 = User.objects.create_user(username="dave", password="password")

        self.post = Post.objects.create(owner=self.user1, title="Test Post", content="Content here")

    def test_user_can_create_save(self):
        """
        A logged-in user can save a post.
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Save.objects.count(), 1)
        self.assertEqual(Save.objects.first().owner, self.user1)

    def test_user_cannot_create_duplicate_save(self):
        """
        A user cannot save the same post twice.
        """
        self.client.login(username="Lewis", password="password")
        self.client.post("/saves/", {"post": self.post.id})
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Possible Duplication", str(response.data))

    def test_anonymous_user_cannot_create_save(self):
        """
        Anonymous users cannot save posts.
        """
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_view_save_list(self):
        """
        Any user can view the list of saves.
        """
        Save.objects.create(owner=self.user1, post=self.post)
        response = self.client.get("/saves/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_can_delete_own_save(self):
        """
        A user can delete their own save.
        """
        save = Save.objects.create(owner=self.user1, post=self.post)
        self.client.login(username="Lewis", password="password")
        response = self.client.delete(f"/saves/{save.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Save.objects.count(), 0)

    def test_user_cannot_delete_other_users_save(self):
        """
        Users cannot delete saves they do not own.
        """
        save = Save.objects.create(owner=self.user1, post=self.post)
        self.client.login(username="dave", password="password")
        response = self.client.delete(f"/saves/{save.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Save.objects.count(), 1)

    def test_user_save_list_only_shows_own_saves(self):
        """
        The /my-saves/ endpoint should only return saves for the logged-in user.
        """
        Save.objects.create(owner=self.user1, post=self.post)
        Save.objects.create(owner=self.user2, post=self.post)

        self.client.login(username="Lewis", password="password")
        response = self.client.get("/my-saves/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["owner"], "Lewis")