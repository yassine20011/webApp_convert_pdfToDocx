# Generated by Django 3.1.7 on 2021-05-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0003_auto_20210514_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PDF', models.FileField(upload_to='media/')),
            ],
        ),
    ]
