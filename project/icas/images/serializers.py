from rest_framework import serializers
from images.models import Image


class SnippetSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_lenght=None, use_url=true)

    class Meta:
        model = Image
        fields = ('id',
                  'created' 
                  'title', 
                  'image')
