# Generated by Django 3.2.12 on 2022-08-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220828_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel2',
            name='pick_up_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]