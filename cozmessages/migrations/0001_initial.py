# Generated by Django 2.2.5 on 2022-11-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cozmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=140)),
                ('text', models.CharField(max_length=140)),
                ('roomname', models.CharField(max_length=140)),
            ],
        ),
    ]
