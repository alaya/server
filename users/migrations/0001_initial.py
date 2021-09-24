# Generated by Django 3.2.6 on 2021-09-24 10:20

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cities_light', '0011_auto_20210924_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50, verbose_name='Имя Фамилия')),
                ('login', models.CharField(max_length=20, unique=True, verbose_name='login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('description', models.CharField(max_length=254, null=True, verbose_name='О себе')),
                ('avatar', models.ImageField(null=True, upload_to='uploads/')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='cities_light.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
