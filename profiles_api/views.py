from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,filters 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers,models,permissions

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handle creating and updating profiles"""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()

	"""Adding additional authentication and permissions to viewset"""
	authentication_classes = (TokenAuthentication, )
	permission_classes = (permissions.UpdateOwnProfile, )

	"""Adding search filters"""
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
	"""Hanlde creating user authentication tokens"""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
	"""Handles creating, reading, and updating profile feed items"""

	authentication_classes = (TokenAuthentication, )
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	permission_classes = (
		permissions.UpdateOwnStatus,
	IsAuthenticated )

	def perform_create(self, serializer):
		"""Sets the user profile to the logged in user"""
		serializer.save(user_profile=self.request.user)