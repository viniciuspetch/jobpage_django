# Generated by Django 2.2.4 on 2019-09-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190902_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='curriculum',
            field=models.FileField(blank=True, null=True, upload_to='cv_upload/'),
        ),
    ]
