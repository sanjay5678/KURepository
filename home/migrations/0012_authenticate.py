# Generated by Django 4.0 on 2022-01-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_applications_photo_approved_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mob', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
