# Generated by Django 5.0.1 on 2024-05-21 17:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('condition', models.CharField(choices=[('NEW', 'NEW'), ('USED', 'USED')], max_length=10)),
                ('authenticity', models.CharField(choices=[('ORIGINAL', 'ORIGINAL'), ('REFURBISHED', 'REFURBISHED')], max_length=50)),
                ('brand', models.CharField(choices=[('SAMSUNG', 'SAMSUNG'), ('LG', 'LG'), ('WALTON', 'WALTON'), ('OTHER', 'OTHER')], max_length=10)),
                ('model', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product/images/')),
                ('description', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('Negotiable', models.BooleanField(blank=True, default=False)),
                ('category', models.ManyToManyField(to='products.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile')),
            ],
        ),
    ]
