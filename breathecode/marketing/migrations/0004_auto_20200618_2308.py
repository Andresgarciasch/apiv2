# Generated by Django 3.0.7 on 2020-06-18 23:08

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20200618_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(default=None, max_length=150, null=True)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('phone',
                 phonenumber_field.modelfields.PhoneNumberField(blank=True,
                                                                default=None,
                                                                max_length=128,
                                                                null=True,
                                                                region=None)),
                ('language', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='formentry',
            name='contact',
            field=models.ForeignKey(default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='marketing.Contact'),
        ),
    ]
