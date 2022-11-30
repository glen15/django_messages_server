# Generated by Django 3.0 on 2022-11-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozmessages', '0004_auto_20221129_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('githubId', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('getMethod', models.BooleanField(default=False)),
                ('postMethod', models.BooleanField(default=False)),
                ('deleteMethod', models.BooleanField(default=False)),
            ],
        ),
    ]