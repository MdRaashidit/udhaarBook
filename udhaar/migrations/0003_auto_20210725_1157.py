# Generated by Django 3.1.2 on 2021-07-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udhaar', '0002_transactions_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='total',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]