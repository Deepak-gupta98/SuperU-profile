from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_image/')

    class Meta:
        db_table = 'SuperU_profile'
    
    def __str__(self):
        return self.name