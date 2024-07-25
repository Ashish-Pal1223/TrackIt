# Generated by Django 4.2.4 on 2024-06-10 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_action_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
