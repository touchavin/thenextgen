# Generated by Django 3.2.4 on 2021-06-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwed', '0004_auto_20210630_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='netxgen',
            name='Day',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='netxgen',
            name='Time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
