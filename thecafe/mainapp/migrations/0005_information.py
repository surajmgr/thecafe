# Generated by Django 2.2.4 on 2019-12-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_carousel_imgname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
