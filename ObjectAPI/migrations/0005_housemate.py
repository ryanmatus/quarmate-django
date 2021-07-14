# Generated by Django 3.2 on 2020-11-10 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ObjectAPI', '0004_auto_20201110_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housemate',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ObjectAPI.person')),
                ('housemate_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=60)),
                ('guests', models.ManyToManyField(to='ObjectAPI.Guest')),
            ],
            bases=('ObjectAPI.person',),
        ),
    ]