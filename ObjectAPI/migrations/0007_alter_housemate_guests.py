# Generated by Django 3.2 on 2020-11-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ObjectAPI', '0006_auto_20201111_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemate',
            name='guests',
            field=models.ManyToManyField(blank=True, null=True, to='ObjectAPI.Guest'),
        ),
    ]
