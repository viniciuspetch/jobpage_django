# Generated by Django 2.2.4 on 2019-09-02 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190902_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='datetime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
