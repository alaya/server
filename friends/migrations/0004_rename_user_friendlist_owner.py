# Generated by Django 3.2.6 on 2021-10-07 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_alter_friendlist_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendlist',
            old_name='user',
            new_name='owner',
        ),
    ]