from django.urls import path
from .views import (
    CourseCreate,
    CourseListView,
    CourseUpdate,
    CoursePartialUpdate,
    CourseDelete,
)

urlpatterns = [
    path("courses/create/", CourseCreate.as_view(), name="course-create"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/update/", CourseUpdate.as_view(), name="course-update"),
    path("courses/<int:pk>/putch/", CoursePartialUpdate.as_view(), name="course-partial-update"),
    path("courses/<int:pk>/delete/", CourseDelete.as_view(), name="course-delete"),
]