from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='project_images/')
    body = models.TextField()

    def summary(self):
        return self.body[0:100]
    def __str__(self):
        return self.title