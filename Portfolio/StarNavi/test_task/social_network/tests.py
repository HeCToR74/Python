from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer


class PostTestCase(TestCase):
    def setUp(self):
    	user = User.objects.create(username="User", password="1234q1234w")
    	post = Post.objects.create(user=user, title="Title of a post", body="Body of a post")
    	post.like += 1
    	post.unlike += 1
    	post.unlike += 1
    	post.save()

    def test_post(self):
    	post = Post.objects.get(id=1)
    	self.assertEquals(post.title, 'Title of a post')

    def test_put(self):
    	post = Post.objects.get(id=1)
    	self.assertEquals(post.like, 1)
    	self.assertEquals(post.unlike, 2)
   
