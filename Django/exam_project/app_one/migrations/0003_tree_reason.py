# Generated by Django 4.1.1 on 2022-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_tree'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='reason',
            field=models.TextField(default='i like it'),
        ),
    ]