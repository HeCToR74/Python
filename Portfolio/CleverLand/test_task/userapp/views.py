from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        if request.user.is_superuser:
            user = request.data.get('user')
            serializer = UserSerializer(data=user)
            if serializer.is_valid(raise_exception=True):
                user_saved = serializer.save()
            return Response({"success": "User '{} {}' created successfully".format(user_saved.name, user_saved.lastname)})
        return Response({"User {} is not superuser".format(request.user)})

    def put(self, request, pk):
        if request.user.is_superuser:
            saved_user = get_object_or_404(User.objects.all(), pk=pk)
            data = request.data.get('user')
            print(data)
            serializer = UserSerializer(instance=saved_user, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                user_saved = serializer.save()
            return Response({
                "success": "User {} {} updated successfully".format(user_saved.name, user_saved.lastname)
            })
        return Response({"User {} is not superuser".format(request.user)})

    def delete(self, request, pk):
        if request.user.is_superuser:
            user = get_object_or_404(User.objects.all(), pk=pk)
            user.delete()
            return Response({
                "message": "User with id `{}` has been deleted.".format(pk)
            }, status=204)
        return Response({"User {} is not superuser".format(request.user)})
