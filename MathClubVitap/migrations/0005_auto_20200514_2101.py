# Generated by Django 3.0.5 on 2020-05-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MathClubVitap', '0004_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='data/'),
        ),
    ]