# Generated by Django 3.2.9 on 2022-01-27 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220126_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='using',
            options={'ordering': ['-date']},
        ),
    ]
