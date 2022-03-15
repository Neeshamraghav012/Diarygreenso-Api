from operator import mod
from pyexpat import model
from rest_framework import serializers

from .models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = ['name', 'author', 'description', 'about', 'link', 'overall_rating', 
        
        'price', 'catagory', 'platform', 'released_date', 'country', 'language', 'price', 

        'duration', 'certificate', 'material_type', 'added_by']