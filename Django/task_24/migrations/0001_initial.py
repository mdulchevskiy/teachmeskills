# Generated by Django 3.0.5 on 2020-04-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NatureImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default=None, max_length=255)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('comment', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
