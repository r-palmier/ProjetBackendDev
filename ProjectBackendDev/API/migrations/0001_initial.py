# Generated by Django 5.1.6 on 2025-03-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('profession', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('degree', models.CharField(max_length=255)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
