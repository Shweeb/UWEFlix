# Generated by Django 4.1.5 on 2023-01-14 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0016_userpurchasehistory_clubpurchasehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubpurchasehistory',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpurchasehistory',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
