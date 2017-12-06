from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

import hashlib

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
                    view_name='snippet-highlight', 
                    format='html')

    class Meta:
        model = Snippet
        fields = ('id', 
                  'title', 
                  'code',
                  'highlight', 
                  'linenos', 
                  'language',
                  'owner',
                  'style',
                  'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
 #   snippets = serializers.HyperlinkedRelatedField(
 #               many=True, 
 #               read_only=True,
 #               view_name='snippet-detail')
    
    class Meta:
        model = User
        fields = ('id', 
                  'first_name',
                  'last_name',
#                  'snippets',
                  'username', 
                  'password',
                  'url')
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            user = super(UserSerializer, self).create(validated_data)
            user.save()
            return user    
