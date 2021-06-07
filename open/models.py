from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.views import UserModel
# from django.contrib.auth imp

# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(UserModel,models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('open:story_detail',kwargs={'pk':self.pk})

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

class Review(models.Model):
    author = models.CharField(max_length=256)
    story = models.ForeignKey(Story,on_delete=models.CASCADE,related_name='reviews')
    text = models.TextField(max_length=200)
    added_date = models.DateTimeField(default=timezone.now())
    approved_review = models.BooleanField(default=False)

    def approve_review(self):
        self.approved_review=True
        self.save()

    def get_absolute_url(self):
        return reverse('open:story_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.text
