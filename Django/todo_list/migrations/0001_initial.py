# Generated by Django 3.0.3 on 2020-02-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(default=None, max_length=255)),
                ('priority', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
    ]
