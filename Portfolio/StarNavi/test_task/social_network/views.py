from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, User
from .serializers import PostSerializer, UserSerializer

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)        
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')        
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)        
        return Response({"users": serializer.data})
