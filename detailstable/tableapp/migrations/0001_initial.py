# Generated by Django 3.2.9 on 2022-02-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=15)),
                ('salary', models.IntegerField(max_length=10)),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach_name', models.CharField(max_length=10)),
                ('teach_address', models.CharField(max_length=30)),
                ('teach_email', models.EmailField(max_length=15)),
                ('teach_salary', models.IntegerField(max_length=10)),
                ('teach_phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
