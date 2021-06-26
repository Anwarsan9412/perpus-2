# Generated by Django 3.2.4 on 2021-06-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_pinjambuku'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='pinjambuku',
            name='tanggal_berakhir',
            field=models.DateField(blank=True, default='2021-06-29', null=True),
        ),
    ]