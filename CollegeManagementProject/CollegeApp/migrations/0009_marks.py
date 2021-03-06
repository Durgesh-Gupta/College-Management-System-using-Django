# Generated by Django 3.1.3 on 2020-12-27 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeApp', '0008_leave_on_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('out_of_m', models.IntegerField(default=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.course')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.usermodel')),
            ],
        ),
    ]
