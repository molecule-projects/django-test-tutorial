from http import HTTPStatus as status

from django.test import TestCase
from django.shortcuts import reverse

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


class PostViewTestCase(TestCase):

    def setUp(self):
        self.first_post = Post.objects.create(
            name="example", post="example post")
        self.second_post = Post.objects.create(
            name="example2", post="example post2")
        self.third_post = Post.objects.create(
            name="example3", post="example post3")

    def test_post_list_view(self):
        # 一覧viewのURL
        list_url = reverse('app:list')
        # viewの呼び出し
        response = self.client.get(list_url)
        # 呼び出しが成功したか確認
        self.assertEqual(response.status_code, status.OK)
        # 呼び出されたviewに期待される内容が存在するか
        self.assertContains(response, 'example')
        self.assertContains(response, 'example post2')
        self.assertContains(response, 'example post3')  # nameの代わりにpostも確認できる
        # どのテンプレートが使われているか確認
        self.assertTemplateUsed(response, 'app/list.html')

    def test_post_detail_view(self):
        # 詳細viewのURL
        detail_url = reverse('app:detail', kwargs={'id': self.first_post.pk})
        # viewの呼び出し
        response = self.client.get(detail_url)
        # 呼び出しが成功したか確認
        self.assertEqual(response.status_code, status.OK)
        self.assertContains(response, 'example')
        self.assertTemplateUsed(response, 'app/detail.html')

    def test_post_detail_view_failure(self):
        # 詳細viewのURL
        detail_url = '1234/'
        # viewの呼び出し
        response = self.client.get(detail_url)
        # 失敗したことを確認
        self.assertEqual(response.status_code, 404)

    def test_post_list_view_can_create_data(self):
        # 一覧viewのURL
        list_url = reverse('app:list')
        data = {
            'name': 'example 4',
            'post': 'example post4',
        }
        response = self.client.post(list_url, data=data)
        self.assertEqual(response.status_code, status.FOUND)
        redirect_url = reverse('app:list')
        self.assertRedirects(response, redirect_url)
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 4)
