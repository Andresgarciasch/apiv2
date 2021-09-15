# Generated by Django 3.1.2 on 2020-10-12 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0011_auto_20201006_0058'),
        ('events', '0013_auto_20201012_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventbrite_id', models.CharField(blank=True, max_length=30, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy',
                 models.ForeignKey(blank=True,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.academy')),
                ('organization',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organization')),
            ],
        ),
    ]
