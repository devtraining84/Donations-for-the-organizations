# Generated by Django 3.2.12 on 2022-08-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220828_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel2',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='city',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='pick_up_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='pick_up_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='pick_up_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel2',
            name='zip_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
