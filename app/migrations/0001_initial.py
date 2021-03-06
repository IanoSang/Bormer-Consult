# Generated by Django 4.0.5 on 2022-06-23 18:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png', max_length=255)),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('citizenship', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='app.consultation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='app.profile'),
        ),
    ]
