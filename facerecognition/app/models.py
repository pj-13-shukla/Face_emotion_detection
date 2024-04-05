from django.db import models

# Create your models here.
class FaceRecognition(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to= 'images/')
    
    
    def __str__(self):
        return str(self.record_date)

# class Image(models.Model):
#     name = models.CharField(max_length=100, default='Default Name')
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')