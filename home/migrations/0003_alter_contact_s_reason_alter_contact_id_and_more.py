# Generated by Django 4.0 on 2021-12-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_s_reason_contact_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='S_Reason',
            field=models.TextField(default="Didn't Checked", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
    ]
