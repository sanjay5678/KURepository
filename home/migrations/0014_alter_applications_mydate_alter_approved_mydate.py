# Generated by Django 4.0 on 2022-01-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_authenticate_sq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='myDate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='approved',
            name='myDate',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
