# Generated by Django 3.1.6 on 2021-02-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medcard', '0005_auto_20210218_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalProcedures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]