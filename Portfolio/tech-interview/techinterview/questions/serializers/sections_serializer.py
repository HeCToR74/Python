from rest_framework import serializers
from questions.models import Sections


class SectionsSerializer(serializers.ModelSerializer):
    """Serializer for Sections model"""

    class Meta:
        model = Sections
        # without id because id specified in URL
        fields = ('id', 'name',)
