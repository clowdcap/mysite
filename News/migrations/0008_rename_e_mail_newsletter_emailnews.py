# Generated by Django 3.2.6 on 2021-09-03 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_newsletter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='e_mail',
            new_name='emailnews',
        ),
    ]
