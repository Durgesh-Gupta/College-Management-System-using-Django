# Generated by Django 3.1.3 on 2020-12-27 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeApp', '0007_auto_20201227_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='on_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]