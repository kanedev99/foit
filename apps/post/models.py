from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by_user = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created", "-updated"]
