from django.urls import path

from .api_views import CourseListView,CourseCreateView,CourseDetailView

urlpatterns=[
    path('courses/all',CourseListView.as_view(),name='course_list'),
    path('courses/create/',CourseCreateView.as_view(),name='course_create'),
    path('courses/detail/<int:pk>/',CourseDetailView.as_view(),name='course_create'),
]