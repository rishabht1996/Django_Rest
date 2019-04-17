# Generated by Django 2.2 on 2019-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('ver_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
