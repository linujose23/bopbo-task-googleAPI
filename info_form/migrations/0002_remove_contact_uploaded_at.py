# Generated by Django 3.1 on 2020-10-15 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='uploaded_at',
        ),
    ]
