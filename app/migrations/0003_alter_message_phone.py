# Generated by Django 4.0.5 on 2022-06-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_message_subject_alter_message_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
