from django.db import models

class Image(models.Model):
#    created = models.DateTimeField(auto_now_add=True)
#    title = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='media', default='media/out/out.jpg')
    
    class Meta:
        ordering = ('id',)