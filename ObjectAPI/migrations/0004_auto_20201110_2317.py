# Generated by Django 3.2 on 2020-11-10 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False
    
    dependencies = [
        ('ObjectAPI', '0003_alter_person_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ObjectAPI.person')),
                ('guest_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('ObjectAPI.person',),
        ),
        migrations.RenameField(
            model_name='person',
            old_name='id',
            new_name='person_id',
        ),
    ]