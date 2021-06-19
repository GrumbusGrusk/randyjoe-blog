from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Albums(models.Model):
    title = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000)
    release_date = models.DateField()

    def __str__(self):
        return self.title
