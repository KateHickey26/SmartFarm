from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# class UserProfile(models.Model):
#     # Links UserProfile to a User model instance.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # The additional attributes we wish to include.
#     profile_image = models.ImageField(upload_to='profile_images', blank=True)
#
#     def __str__(self):
#         return self.user.username
#
# # use to have colours for each type of sensor?
# class SensorStatus(models.Model):
#     status = models.CharField(max_length=32)
#
#     class Meta:
#         verbose_name_plural = "Sensor statuses"
#
#     def __unicode__(self):
#         return self.status
#
#     def __str__(self):
#         return self.status
#
# class Sensor(models.Model):
#     name = models.CharField(max_length=32)
#     coord_v = models.FloatField()
#     coord_h = models.FloatField()
#     status = models.ForeignKey(SensorStatus, on_delete=models.CASCADE)
#
#
#     def __unicode__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
