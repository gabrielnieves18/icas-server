from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly, RegisterUser
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import permissions, generics, renderers
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

# ViewSets define the view behavior.
class SnippetViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    serializer_class = SnippetSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Snippet.objects.filter(owner=user.id)
        
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (RegisterUser,)
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return User.objects.filter(id=user.id)
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        serializer.validated_data['password'] = hashed_password 
        user = super(UserViewSet, self).perform_create(serializer) # create a user
        
    def perform_update(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        #instance = serializer.save()
        serializer.validated_data['password'] = hashed_password 
        user = super(UserViewSet, self).perform_update(serializer) # create a user
        