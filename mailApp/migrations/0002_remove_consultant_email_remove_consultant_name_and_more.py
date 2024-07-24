# Generated by Django 5.0.6 on 2024-07-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='name',
        ),
        migrations.AddField(
            model_name='consultant',
            name='consultant_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
