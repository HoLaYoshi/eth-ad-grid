# Generated by Django 2.0.1 on 2018-06-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
