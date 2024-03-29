# Generated by Django 4.2.1 on 2023-07-15 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0005_remove_insuranceininfo_patient_and_more'),
        ('healthfinda', '0006_alter_review_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insuranceininfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Insurancecarrier', models.CharField(default='Unknown', max_length=200)),
                ('plan', models.CharField(default='Unknown', max_length=200)),
                ('Contact', models.CharField(default='Unknown', max_length=200)),
                ('policynumber', models.CharField(default='Unknown', max_length=200)),
                ('groupnumber', models.CharField(default='Unknown', max_length=200)),
                ('socialsecuritynumber', models.CharField(default='Unknown', max_length=200)),
                ('patient', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Registration.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='healthinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='Unknown', max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.doctorprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Emergencycontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=200)),
                ('relation', models.CharField(default='Unknown', max_length=200)),
                ('Contact', models.CharField(default='Unknown', max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.patientprofile')),
            ],
        ),
    ]
