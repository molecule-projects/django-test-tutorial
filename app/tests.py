from django.test import TestCase

from .models import Post


class PostModelTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(name="example", post="example post")

    def test_model_can_create(self):
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 1)

    def test_model_can_create_2(self):
        Post.objects.create(name="example2", post="example post2")
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 2)
