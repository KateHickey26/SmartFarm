

# Create your models here.

# dont need this model as we dont need any extra attributes outside the
# normal django user model?
# class UserProfile(models.Model):
#     # Links UserProfile to a User model instance.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     username = models.CharField(blank=False, max_length=25, default="username")
#
#     # method to return a meaningful value when a string
#     # representation of a user profile is requested
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
