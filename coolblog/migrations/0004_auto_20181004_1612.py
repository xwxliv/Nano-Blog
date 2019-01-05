# Generated by Django 2.1.2 on 2018-10-04 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0003_auto_20181004_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'])]),
        ),
    ]
