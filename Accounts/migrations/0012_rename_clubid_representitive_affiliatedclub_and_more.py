# Generated by Django 4.1.5 on 2023-01-13 23:25

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_club_discount_alter_club_streetno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representitive',
            old_name='clubID',
            new_name='affiliatedClub',
        ),
        migrations.RenameField(
            model_name='representitive',
            old_name='userID',
            new_name='studentRepresentitive',
        ),
        migrations.AlterField(
            model_name='club',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='club',
            name='landlineNo',
            field=models.CharField(max_length=200, null=True, validators=[Accounts.models.isLandlineNumber]),
        ),
        migrations.AlterField(
            model_name='club',
            name='mobileNo',
            field=models.CharField(max_length=20, null=True, validators=[Accounts.models.isMobileNumber]),
        ),
    ]
