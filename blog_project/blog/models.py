from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    STATUS_CHOICES =(("draft","Draft"),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=64,unique_for_date='publish')
    author=models.ForeignKey(User,related_name ="blog_post",on_delete=models.CASCADE)
    body=models.TextField(max_length=264)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=64,choices=STATUS_CHOICES,default="draft")

    class Meta:
        ordering=("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=(self.publish.year,self.publish.strftime("%m"),self.publish.strftime("%d"),self.slug))






