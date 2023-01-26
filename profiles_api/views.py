from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers,models,permissions

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handle creating and updating profiles"""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()

	"""Adding additional authentication and permissions to viewset"""
	authentication_classes = (TokenAuthentication, )
	permission_classes = (permissions.UpdateOwnProfile, )
