
from rest_framework import generics, filters
from .models import Course
from .serializers import CourseSerializer


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()

        price = self.request.query_params.get("price")
        if price:
            queryset = queryset.filter(price=price)

        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset


class CourseCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursePartialUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ["patch", "options", "head"]


class CourseDelete(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer