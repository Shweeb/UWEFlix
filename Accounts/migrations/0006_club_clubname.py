# Generated by Django 4.1.5 on 2023-01-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_rename_name_employee_firstname_employee_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='clubName',
            field=models.CharField(default='Archery', max_length=200),
            preserve_default=False,
        ),
    ]