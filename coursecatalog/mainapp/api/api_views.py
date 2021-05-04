from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.filters import SearchFilter
from .serializers import CourseSerializer
from ..models import Course
from rest_framework import generics
from django_filters  import rest_framework as filters


class CourseFilter(filters.FilterSet):

    class Meta:
        model = Course
        fields= {
            'id': ['icontains'],
            'title': ['icontains'],
            'datestart': ['iexact', 'lte', 'gte'],
            'dateend': ['iexact', 'lte', 'gte'],
        }

class CourseListView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filterset_class = CourseFilter
    lookup_field = 'id'

class CourseCreateView(CreateAPIView):
    serializer_class = CourseSerializer

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()