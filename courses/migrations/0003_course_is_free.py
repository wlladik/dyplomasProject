# Generated by Django 4.1.4 on 2023-01-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_image_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Free?'),
        ),
    ]