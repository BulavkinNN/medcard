# Generated by Django 3.1.6 on 2021-02-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medcard', '0011_analysis_inspection_operation_survey_vaccination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
        migrations.AddField(
            model_name='analysis',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AddField(
            model_name='operation',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
    ]
