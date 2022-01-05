from django.db import models
import uuid  # for unique id

# Create your models here.


class Project(models.Model):
    project_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="project-images/",  null=True, blank=True)

    class Meta:
        ordering = ['-project_id']


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}--{self.description}"
