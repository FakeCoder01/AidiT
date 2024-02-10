from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class Photo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="static/media/", default="static/media/d.png")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    