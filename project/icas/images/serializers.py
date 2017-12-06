from rest_framework import serializers
from images.models import Image

from model import Model


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
	
    m = Model(image_uri=image)
	
    objects = m.inferense()
    
    print(objects)
    	
    class Meta:
        model = Image
        fields = ('id',
                  'created',
                  'title',
                  'image')
