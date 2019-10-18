# Generated by Django 2.2.6 on 2019-10-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DonationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donor_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.BinaryField()),
                ('registered', models.BinaryField()),
                ('opened_link', models.BinaryField()),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfg_team_3.Customer')),
                ('donor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfg_team_3.Donor')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfg_team_3.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfg_team_3.Customer')),
                ('donor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfg_team_3.Donor')),
            ],
        ),
    ]
