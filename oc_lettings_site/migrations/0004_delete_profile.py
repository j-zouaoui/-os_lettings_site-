# Generated by Django 3.0 on 2022-05-04 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_auto_20220504_1626'),
    ]

    state_operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
    ]

