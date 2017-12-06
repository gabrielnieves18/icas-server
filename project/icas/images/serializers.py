from rest_framework import serializers
from images.models import Image

from model import Model


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
    print('\n\nThe image = {}\n\n'.format(image))
	
    modl = Model()
	
    objects = modl.inferense(image_uri=image)
    
    print(objects)	
    
    class Meta:
        model = Image
        fields = ('id',
                  'created',
                  'title',
                  'image')
