# Generated by Django 3.2.4 on 2021-06-20 14:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210620_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_buku', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('penerbit', models.CharField(blank=True, max_length=255, null=True)),
                ('tahun_terbit', models.DateField(blank=True, null=True)),
                ('judul_buku', models.CharField(max_length=255)),
                ('cover_pic', models.ImageField(blank=True, default='python.jpg', null=True, upload_to='images')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('buku_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bukucategory')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
