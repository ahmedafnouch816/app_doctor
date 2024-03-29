# Generated by Django 4.2.1 on 2023-07-14 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
        ('healthfinda', '0004_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(default='Nothing')),
                ('timestamp', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.patientprofile')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.doctorprofile')),
            ],
        ),
    ]
