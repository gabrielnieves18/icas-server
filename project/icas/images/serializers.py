from rest_framework import serializers
from images.models import Image

from models import Model


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
	
	model = Model(image_uri=image)
	
	objects = model.inferense()
	
	print(objects)
	
    class Meta:
        model = Image
        fields = ('id',
                  'created',
                  'title',
                  'image')
