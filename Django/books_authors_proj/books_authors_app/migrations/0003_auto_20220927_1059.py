# Generated by Django 2.2.4 on 2022-09-27 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_publisher_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publisher',
            new_name='Author',
        ),
    ]
