# Generated by Django 3.2.4 on 2021-06-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_buku_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinjambuku',
            name='kode_buku',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.buku'),
        ),
    ]