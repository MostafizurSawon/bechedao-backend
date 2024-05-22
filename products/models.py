from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name

CONDITION_CHOICES = [
    ('NEW', 'NEW'),
    ('USED', 'USED'),
]

AUTHENTICITY_CHOICES = [
    ('ORIGINAL', 'ORIGINAL'),
    ('REFURBISHED', 'REFURBISHED'),
]

BRAND_CHOICES = [
    ('SAMSUNG', 'SAMSUNG'),
    ('LG', 'LG'),
    ('WALTON', 'WALTON'),
    ('OTHER', 'OTHER'),
]

class Product(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ManyToManyField(Category)
    condition = models.CharField(choices = CONDITION_CHOICES, max_length = 10)
    authenticity = models.CharField(choices = AUTHENTICITY_CHOICES, max_length = 50)
    brand = models.CharField(choices = BRAND_CHOICES, max_length = 10)
    model = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="product/images/")
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    Negotiable = models.BooleanField(default=False, blank=True)
    sold = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return f"{self.name} of Mr. {self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"User : {self.reviewer.user.first_name} ; Product: {self.recipe.user.first_name}"