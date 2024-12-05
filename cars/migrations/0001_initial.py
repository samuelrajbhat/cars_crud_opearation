# Generated by Django 5.1.3 on 2024-12-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=100)),
                ('car_version', models.CharField(max_length=3)),
                ('car_model', models.CharField(max_length=15)),
                ('car_company', models.CharField(max_length=100)),
                ('car_manufactured_year', models.DateField()),
            ],
        ),
    ]