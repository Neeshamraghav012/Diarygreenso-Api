
from django.urls import path, include
from rest_framework import routers
from diary_apis.views import RatingView



urlpatterns = [

    path('ratingss/', RatingView, name = "course-rating"),

]
