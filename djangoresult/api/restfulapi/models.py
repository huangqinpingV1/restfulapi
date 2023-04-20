from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.CharField(max_length = 100,default='')
    singer = models.CharField(max_length=100,default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music'
