# Generated by Django 3.1 on 2020-10-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100, null=True)),
                ('Email', models.EmailField(default='', max_length=254)),
                ('Mobile', models.CharField(default='', max_length=12)),
                ('Message', models.TextField(default='', max_length=400)),
                ('files', models.FileField(null=True, upload_to='', verbose_name='files_to_upload')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
