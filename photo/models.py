from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.author.username +" " + self.created.strftime("%Y/%m/%d")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])