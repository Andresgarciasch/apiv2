# Generated by Django 3.1.6 on 2021-04-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='language',
        ),
        migrations.AddField(
            model_name='asset',
            name='gitpod',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('OK', 'Ok'),
                                            ('WARNING', 'Warning'),
                                            ('ERROR', 'Error')],
                                   default='OK',
                                   max_length=20),
        ),
        migrations.AddField(
            model_name='asset',
            name='status_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
