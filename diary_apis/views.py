from django.shortcuts import render
from .serializers import CourseSerializer, RatingSerializer, WatchlistSerializer, TotalRatingSerializer
from django.http import HttpResponse, JsonResponse
from .models import Course, Rating, TotalRating, Watchlist
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.parsers import JSONParser

#print(dir(viewsets.ModelViewSet))
# Generic class based view.
class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer
   permission_classes = (permissions.IsAuthenticated,)


class RatingViewSet(viewsets.ModelViewSet):

  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  

# Customizable Function based view.
@api_view(['GET'])
def CourseView(request):
   
   snippet = Course.objects.all()
   if request.method == 'GET':
      serializer = CourseSerializer(snippet, many = True)
      return JsonResponse(serializer.data, safe=False)


# Customizable class based view
class SnippetList(APIView):

   def get(self, request, format=None):
      snippets = Course.objects.all()
      serializer = CourseSerializer(snippets, many=True)

      return Response(serializer.data)


   def post(self, request, *args, **kwargs):

       serializer = CourseSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       Course = serializer.save()

       return Response({
           "status": "saved",
       })


   #permission_classes = [permissions.IsAuthenticatedOrReadOnly]