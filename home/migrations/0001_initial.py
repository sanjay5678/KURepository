# Generated by Django 4.0 on 2021-12-31 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upiid', models.CharField(max_length=200, null=True)),
                ('amount', models.IntegerField()),
                ('paymentdate', models.DateField()),
                ('cname', models.CharField(max_length=200, null=True)),
                ('fname', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('mob', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('tsubmit', models.CharField(max_length=200, null=True)),
                ('ftsubmit', models.CharField(max_length=200, null=True)),
                ('equalexam', models.CharField(max_length=200, null=True)),
                ('university', models.CharField(max_length=200, null=True)),
                ('monthyear', models.CharField(max_length=200, null=True)),
                ('supname', models.CharField(max_length=200, null=True)),
                ('supdept', models.CharField(max_length=200, null=True)),
                ('supwadd', models.CharField(max_length=200, null=True)),
                ('admissionorder', models.FileField(null=True, upload_to='')),
                ('supreport', models.FileField(null=True, upload_to='')),
                ('tthesis', models.FileField(null=True, upload_to='')),
                ('yearofadd', models.IntegerField(null=True)),
                ('time', models.CharField(max_length=200)),
                ('ptime', models.CharField(max_length=90)),
                ('onTime', models.CharField(max_length=90)),
                ('onTimef', models.FileField(null=True, upload_to='')),
                ('prephd', models.CharField(max_length=200, null=True)),
                ('article', models.IntegerField(null=True)),
                ('synopsis', models.FileField(null=True, upload_to='')),
                ('dateofsubmission', models.DateField(null=True)),
                ('noc', models.FileField(null=True, upload_to='')),
                ('myDate', models.DateField(null=True)),
                ('sign', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]