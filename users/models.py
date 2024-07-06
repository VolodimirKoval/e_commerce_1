from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from datetime import datetime


def folder_image_autoname(instance, filename):
    now_date = datetime.now()
    return os.path.join(f"users_images/{now_date.year}/{instance.username}/{filename}")


class User(AbstractUser):
    image = models.ImageField(upload_to=folder_image_autoname, null=True, blank=True, verbose_name='Зображення користувача')
    
    class Meta:
        db_table = "Користувачі"
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
    
    def __str__(self):
        return self.username
    