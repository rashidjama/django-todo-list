# Generated by Django 2.2 on 2020-07-23 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_trip', models.DateField()),
                ('end_trip', models.DateField()),
                ('plan', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trip_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_trips', to='login.User')),
                ('trip_joiners', models.ManyToManyField(related_name='joined_trips', to='login.User')),
            ],
        ),
    ]
