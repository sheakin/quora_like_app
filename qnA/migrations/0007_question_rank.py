# Generated by Django 3.0.6 on 2020-06-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnA', '0006_auto_20200527_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]