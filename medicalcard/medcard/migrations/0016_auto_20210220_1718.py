# Generated by Django 3.1.6 on 2021-02-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medcard', '0015_auto_20210220_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='clinical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.clinical'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='medical_procedures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.medicalprocedures'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='my_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.doctor'),
        ),
        migrations.AlterField(
            model_name='vaccination',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medcard.patient'),
        ),
    ]
