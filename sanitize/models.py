from django.db import models
from django.urls import reverse
import uuid


class FbFile(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    file_input = models.FileField(upload_to='media/leads/')
    file_name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Facebook CSV File"
        verbose_name_plural = "Facebook CSV Files"

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return reverse("sanitize:detail", kwargs={"pk": self.uid})
