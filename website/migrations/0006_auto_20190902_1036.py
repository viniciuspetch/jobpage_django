# Generated by Django 2.2.4 on 2019-09-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190902_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]