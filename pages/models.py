from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return '/detail/%i' % self.id