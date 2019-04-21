from rest_framework import status
from rest_framework.generics import ListAPIView

from authorization.models import UserData, Roles
from authorization.serializers import UserDataSerializer
from interviews.models import Interviews
from rest_framework.response import Response


class UserDetailsAPIView(ListAPIView):
    """UserDetailsAPIView"""

    serializer_class = UserDataSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        role = self.request.query_params.get('role')
        queryset = self.model.objects.filter(f_role__name=role) \
            if role else self.model.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):

        auth = UserData.objects.get(f_auth_id=request.user.id)
        role = Roles.objects.get(id=auth.f_role_id)

        if self.request.query_params.get('role'):
            return super().get(request, *args, **kwargs)

        try:
            interviews_recruiter = \
                len(Interviews.objects.filter(status='scheduled', f_recruiter_id=auth.id))
        except Interviews.DoesNotExist:
            interviews_recruiter = False

        try:
            interviews_candidate = \
                Interviews.objects.filter(status='scheduled', f_candidate_id=auth.id)
            if len(interviews_candidate):
                interviews_candidate = interviews_candidate[0].id
        except Interviews.DoesNotExist:
            interviews_candidate = False

        try:
            interviews_expert = Interviews.objects.filter(status='scheduled', f_expert_id=auth.id)
            if len(interviews_expert):
                interviews_expert = interviews_expert[0].id
        except Interviews.DoesNotExist:
            interviews_expert = False

        user = {
            'id': request.user.id,
            'login': request.user.username,
            'first': request.user.first_name,
            'last': request.user.last_name,
            'email': request.user.email,
            'role': role.name,
            'avatar': auth.avatar,
            'interviews_recruiter': interviews_recruiter,
            'interviews_candidate': interviews_candidate,
            'interviews_expert': interviews_expert,
        }
        return Response({'user': user}, status=status.HTTP_200_OK)
