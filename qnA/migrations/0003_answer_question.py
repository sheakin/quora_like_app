# Generated by Django 3.0.6 on 2020-05-24 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qnA', '0002_auto_20200524_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qnA.Question'),
            preserve_default=False,
        ),
    ]