from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='user_profile/images/')
    mobile_no = models.CharField(max_length = 12)
    age = models.IntegerField(default=18)
    sex = models.CharField(choices = SEX_CHOICES, max_length = 10, default="Male")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
