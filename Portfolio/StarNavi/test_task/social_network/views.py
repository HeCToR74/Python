from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponseForbidden


class PostView(APIView):
    # def get(self, request):
    #     print(request.user)
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')  
        data = {"user": request.user.id, 
                "title": post["title"],
                "body": post["body"]
               }
        serializer = PostSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = {"id": pk,
                "user": saved_post.user.id,
                "title": saved_post.title,
                "body": saved_post.body,
                "like": saved_post.like,
                "unlike": saved_post.unlike,                
                }
        if request.data.get('post') == 'like':
            data["like"] += 1
        if request.data.get('post') == 'unlike':
            data["unlike"] += 1           
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Post '{}' updated successfully".format(post_saved.title)
        })

