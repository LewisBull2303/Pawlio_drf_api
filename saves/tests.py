# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from posts.models import Post
from saves.models import Save

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SaveListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before each test.
        Creates two users and one post.
        """
        self.lewis = User.objects.create_user(
            username="Lewis", password="password"
        )
        self.dave = User.objects.create_user(
            username="dave", password="password"
        )

        self.post = Post.objects.create(
            owner=self.lewis, title="Test Post", description="Test description"
        )

    def test_not_logged_in_user_cannot_save_post(self):
        """
        Test to ensure not logged-in user cannot save posts
        """
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_save_post(self):
        """
        Test to ensure logged-in user can save a post
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Save.objects.count(), 1)
        self.assertEqual(Save.objects.first().owner, self.lewis)

    def test_user_cannot_duplicate_save(self):
        """
        Test to ensure user cannot save the same post twice
        """
        self.client.login(username="Lewis", password="password")
        self.client.post("/saves/", {"post": self.post.id})
        response = self.client.post("/saves/", {"post": self.post.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_list_saves(self):
        """
        Test if possible to list saves
        """
        Save.objects.create(
            owner=self.lewis, post=self.post
        )
        response = self.client.get("/saves/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)


class SaveDetailViewTests(APITestCase):

    def setUp(self):
        """
        Creates two users, one post and two saves
        """
        self.lewis = User.objects.create_user(
            username="Lewis", password="password"
        )
        self.dave = User.objects.create_user(
            username="dave", password="password"
        )

        self.post = Post.objects.create(
            owner=self.lewis, title="Test Post", description="Test description"
        )

        self.save1 = Save.objects.create(owner=self.lewis, post=self.post)
        self.save2 = Save.objects.create(owner=self.dave, post=self.post)

    def test_user_can_retrieve_existing_save(self):
        """
        Test if possible to retrieve a save with valid ID
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.get(f"/saves/{self.save1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_save(self):
        """
        Test if possible to retrieve a save which doesn't exist
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.get("/saves/9999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_own_save(self):
        """
        Test if user can delete their own save
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.delete(f"/saves/{self.save1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Save.objects.count(), 1)

    def test_user_cannot_delete_other_user_save(self):
        """
        Test if user cannot delete other users' saves
        """
        self.client.login(username="Lewis", password="password")
        response = self.client.delete(f"/saves/{self.save2.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Save.objects.count(), 2)
