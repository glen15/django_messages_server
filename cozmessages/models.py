from django.db import models

class Cozmessage(models.Model):

    username = models.CharField(max_length=50)
    text = models.CharField(max_length=140)
    roomname = models.CharField(max_length=50)
    date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.username

class Submit(models.Model):

    githubId = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    getMethod = models.BooleanField(default=False)
    postMethod = models.BooleanField(default=False)
    deleteMethod = models.BooleanField(default=False)

    def __str__(self):
        return self.name