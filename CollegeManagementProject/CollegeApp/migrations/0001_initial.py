# Generated by Django 3.1.3 on 2020-12-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_no', models.IntegerField()),
                ('Bname', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=120)),
                ('img', models.ImageField(default='', upload_to='')),
                ('clink', models.CharField(max_length=254)),
                ('desc', models.CharField(default=None, max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.branchmodel')),
            ],
        ),
    ]
