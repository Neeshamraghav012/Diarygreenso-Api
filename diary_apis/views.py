from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions

# Generic class based view.
class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

# Customizable Function based view.
@api_view(['GET'])
def CourseView(request):
   
   snippet = Course.objects.all()
   if request.method == 'GET':
        serializer = CourseSerializer(snippet)
        return Response(serializer.data)

class SnippetList(APIView):

   def get(self, request, format=None):
      snippets = Course.objects.all()
      serializer = CourseSerializer(snippets, many=True)
      return Response(serializer.data)

   permission_classes = [permissions.IsAuthenticatedOrReadOnly]