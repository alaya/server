# Generated by Django 3.2.5 on 2021-07-26 12:29

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_auto_20210716_1532'),
        ('users', '0011_alter_customuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='cities_light.city'),
        ),
    ]