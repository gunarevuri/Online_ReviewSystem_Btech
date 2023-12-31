# Generated by Django 4.2.7 on 2023-11-18 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=50)),
                ('dept_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostel_Name', models.CharField(max_length=150, null=True, unique=True)),
                ('ratings', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=30)),
                ('p_id', models.CharField(max_length=10, unique=True)),
                ('number', models.CharField(max_length=10)),
                ('p_ratings', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.department')),
            ],
        ),
    ]
