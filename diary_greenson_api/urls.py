
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from diary_apis.views import CourseViewSet, CourseView, SnippetList


router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('func-courses/', CourseView),
    path('class-course/', SnippetList.as_view()),
]
