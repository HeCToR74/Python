from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from interviews.models import Interviews
from interviews.serializers import InterviewsSerializer
from authorization.models import UserData


class InterviewsByIdAPIView(RetrieveUpdateDestroyAPIView):
    """handler for GET request"""

    queryset = Interviews.objects.all()
    serializer_class = InterviewsSerializer

    def update(self, request, *args, **kwargs):
        interview_data = Interviews.objects.get(id=kwargs.get('pk'))
        interview_data.f_department_id = request.data['department']
        interview_data.f_candidate_id = UserData.objects.get(f_auth_id=request.data['candidate']).id
        interview_data.f_expert_id = UserData.objects.get(f_auth_id=request.data['expert']).id
        interview_data.interview_date = request.data['interview_date']
        interview_data.location = request.data['location']
        interview_data.latitude = request.data['latitude']
        interview_data.longitude = request.data['longitude']

        interview_data.save()

        serializer = self.get_serializer(interview_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
