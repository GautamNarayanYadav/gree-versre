# Generated by Django 4.1 on 2022-08-31 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_vers', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
