# Generated by Django 2.2 on 2020-07-28 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200723_2134'),
        ('todo', '0002_todo_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='login.User'),
        ),
    ]