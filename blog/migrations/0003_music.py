# Generated by Django 2.2.24 on 2021-06-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField()),
            ],
        ),
    ]
