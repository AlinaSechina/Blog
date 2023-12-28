from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, default="Post Title")
    date = models.DateTimeField( default=timezone.now, editable=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # добавление метода str() для отображения заголовка
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
