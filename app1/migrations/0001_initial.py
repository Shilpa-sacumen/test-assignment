# Generated by Django 5.1.3 on 2024-12-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empno', models.IntegerField()),
                ('Ename', models.CharField(max_length=255)),
                ('sal', models.FloatField()),
                ('job', models.CharField(max_length=100)),
            ],
        ),
    ]