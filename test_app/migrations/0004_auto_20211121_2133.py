# Generated by Django 3.2.9 on 2021-11-21 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_users_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]