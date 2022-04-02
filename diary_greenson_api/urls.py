
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from diary_apis.views import CourseViewSet, CourseView, SnippetList, RatingViewSet
from accounts import urls

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include(urls)),
    path('function-based-courses/', CourseView),
    path('class-based-courses/', SnippetList.as_view()),
    #path('apiview-based-courses/', CourseViewSet),
]
