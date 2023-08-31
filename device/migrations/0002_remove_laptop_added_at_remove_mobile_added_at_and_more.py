# Generated by Django 4.0.5 on 2023-08-31 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='added_at',
        ),
        migrations.AddField(
            model_name='laptop',
            name='bought_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='laptop',
            name='rom',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mobile',
            name='bought_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
