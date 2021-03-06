# Generated by Django 3.1.3 on 2020-12-26 08:27

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CollegeApp', '0002_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('DOB', models.CharField(max_length=70)),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=50)),
                ('Branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.branchmodel')),
                ('position', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.position')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('conatct', models.CharField(default='', max_length=50)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.branchmodel')),
                ('position', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.position')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
