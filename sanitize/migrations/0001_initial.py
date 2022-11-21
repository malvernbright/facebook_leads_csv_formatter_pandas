# Generated by Django 3.2.16 on 2022-11-21 14:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FbFile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('file_input', models.FileField(upload_to='media/leads/')),
                ('file_name', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Facebook CSV File',
                'verbose_name_plural': 'Facebook CSV Files',
            },
        ),
    ]
