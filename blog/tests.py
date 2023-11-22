from django.test import TestCase
from django.urls import reverse

from .models import Blog


class BlogTests(TestCase):
    title = "Test Blog Creation"
    content = "This is a test blog creation content"

    def setUp(self):
        self.blog = Blog.objects.create(
            title=self.title,
            content=self.content
        )

    def test_blog_create_view(self):
        # Ensure the create post view returns a 200 status code
        response = self.client.get(reverse('blog_create'))
        self.assertEqual(response.status_code, 200)

        updated_title = self.title + " From View"

        form_data = {
            'title': updated_title,
            'content': self.content + " from view"
        }

        response = self.client.post(reverse('blog_create'), data=form_data)

        # Check that the post was created successfully
        self.assertEqual(response.status_code, 302)

        # Check that the post is present in the database
        self.assertTrue(Blog.objects.filter(title=updated_title).exists())

    def test_blog_edit_view(self):
        response = self.client.get(reverse('blog_edit', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)

        updated_title = self.title.replace("Creation", "Updated")

        form_data = {
            'title': updated_title,
            'content': self.content.replace("creation", "updated")
        }

        response = self.client.post(reverse('blog_edit', args=[self.blog.id]), data=form_data)

        # Check that the post was updated successfully
        self.assertEqual(response.status_code, 302)

        # Check that the post is updated in the database
        self.assertTrue(Blog.objects.filter(title=updated_title).exists())

    def test_blog_delete(self):
        response = self.client.post(reverse('blog_delete', args=[self.blog.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Blog.objects.filter(title=self.title).exists())

    def test_blog_listing_page(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_page(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('blog_detail', args=[100]))
        self.assertEqual(response.status_code, 404)
