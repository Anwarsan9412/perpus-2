# Generated by Django 3.2.4 on 2021-06-20 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_buku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='user',
        ),
    ]