# Generated by Django 3.2.6 on 2021-12-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='u',
            field=models.ForeignKey(default='ka', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='blogapp.registration'),
        ),
    ]
