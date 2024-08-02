from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=100)
    item_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "items"
