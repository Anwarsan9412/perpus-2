# Generated by Django 3.2.4 on 2021-06-20 06:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_buku', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('judul_buku', models.CharField(max_length=255)),
                ('cover_pic', models.ImageField(blank=True, default='python.jpg', null=True, upload_to='images')),
                ('updated', models.DateField(auto_now=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BukuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buku_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PinjamBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_buku', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tanggal_pinjam', models.DateField(auto_now_add=True)),
                ('tanggal_berakhir', models.DateField(blank=True, null=True)),
                ('kode_buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.buku')),
                ('peminjam_nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='buku_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bukucategory'),
        ),
    ]
