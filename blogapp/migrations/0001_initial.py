# Generated by Django 3.2.6 on 2021-09-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('blog_text', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('fi_password', models.CharField(max_length=15)),
                ('se_password', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10)),
                ('is_tick', models.BooleanField(default=False, verbose_name='I Agree To The Terms and Conditions')),
            ],
        ),
    ]