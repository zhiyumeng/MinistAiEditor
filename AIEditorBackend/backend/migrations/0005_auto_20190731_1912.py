# Generated by Django 2.2.1 on 2019-07-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190731_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tel_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='User tel number'),
        ),
    ]
