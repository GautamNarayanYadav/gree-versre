# Generated by Django 4.1 on 2022-09-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_vers', '0007_alter_contact_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photography',
            old_name='tags',
            new_name='tag1',
        ),
        migrations.AddField(
            model_name='photography',
            name='tag2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photography',
            name='tag3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photography',
            name='tag4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photography',
            name='tag5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]