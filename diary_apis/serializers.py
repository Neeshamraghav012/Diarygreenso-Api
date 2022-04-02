from rest_framework import serializers

from .models import Course, Rating, TotalRating, Watchlist
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = ['name', 'author', 'description', 'about', 'link', 'overall_rating', 
        
        'price', 'catagory', 'platform', 'released_date', 'country', 'language', 'price', 

        'duration', 'certificate', 'material_type', 'added_by']


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id", "username",]


class RatingSerializer(serializers.ModelSerializer):

	#course = CourseSerializer()
	#user = UserSerializer()


	class Meta:

		model = Rating

		fields = ['course', 'user', 'review', 'rating']


class TotalRatingSerializer(serializers.ModelSerializer):

    class Meta:

        model = TotalRating
        fields = ["course", "total_rating"]


class WatchlistSerializer(serializers.ModelSerializer):

    class Meta:

        model = Watchlist
        fields = ["user", "course"]