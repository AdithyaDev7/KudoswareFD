# Generated by Django 5.1 on 2024-08-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=10)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Work_Experience', models.IntegerField()),
                ('Resume', models.FileField(upload_to='resumes/')),
            ],
        ),
    ]
