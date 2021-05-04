from rest_framework import serializers

from ..models import Course


class CourseSerializer(serializers.ModelSerializer):
    title=serializers.CharField(required=True)

    class Meta:
        model = Course
        fields ='__all__'