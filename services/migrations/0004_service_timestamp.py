# Generated by Django 2.1.3 on 2018-12-31 00:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20181231_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
