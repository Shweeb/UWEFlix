# Generated by Django 4.1.5 on 2023-01-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_alter_club_city_alter_club_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='discount',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='club',
            name='streetNo',
            field=models.IntegerField(),
        ),
    ]