# Generated by Django 4.2.6 on 2023-10-23 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emain', models.EmailField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.PositiveIntegerField(max_length=10)),
                ('about', models.TextField(blank=True, null=True)),
                ('position', models.CharField(choices=[('Manager', 'Manager'), ('Developer', 'Developer'), ('HR Manager', 'HR Manager')], max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompanyApp.company')),
            ],
        ),
    ]