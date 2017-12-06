from images.models import Image
from rest_framework import viewsets
from images.serializers import ImageSerializer

from model import Model

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all().order_by('created')

    def perform_create(self, serializer):
    
        uri = serializer.validated_data['image']
        image = super(ImageViewSet, self).perform_create(serializer) # create a user
        
        print('\n\nThe image = {}\n\n'.format(uri))
	
        modl = Model()
	
        objects = modl.inferense(image_uri=uri)
    
        print(objects)	
    
	
