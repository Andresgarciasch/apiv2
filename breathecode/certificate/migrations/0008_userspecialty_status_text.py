# Generated by Django 3.1.4 on 2020-12-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_auto_20201029_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspecialty',
            name='status_text',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]