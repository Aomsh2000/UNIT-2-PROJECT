# Generated by Django 5.1.2 on 2024-11-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=124)),
                ('about', models.EmailField(max_length=254)),
                ('sources', models.TextField()),
                ('image', models.FileField(default='images/default (2).jpg', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
