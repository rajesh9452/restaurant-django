from django.db import models

class Promotion(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    upload_image = models.ImageField(upload_to="promotions/images/", blank=True, null=True)
    upload_video = models.FileField(upload_to="promotions/videos/", blank=True, null=True)
    enable = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title