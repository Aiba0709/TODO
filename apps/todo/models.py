from django.db import models

from apps.users.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_todo",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Названия"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    image = models.ImageField(
        upload_to="todo/",
        verbose_name="Фотография",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Таски"
        verbose_name_plural = "Таск"
        unique_together = ('user', 'title')
