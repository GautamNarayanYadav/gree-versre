# Generated by Django 4.1 on 2022-08-31 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_vers', '0004_alter_contact_address_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
