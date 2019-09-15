from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
    	user = User.objects.create(username="User", password="1234q1234w")
    	Post.objects.create(user=user, title="Title of a post", body="Body of a post")

    def test_post(self):
    	post = Post.objects.get(id=1)
    	self.assertEquals('Title of a post', 'Title of a post')
        
