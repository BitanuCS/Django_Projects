# Generated by Django 3.2.3 on 2021-05-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
    ]
