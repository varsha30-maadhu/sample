# Generated by Django 4.1.4 on 2022-12-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_remove_regmodel_cpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regmodel',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='regmodel',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
