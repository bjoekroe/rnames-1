# Generated by Django 3.2.13 on 2022-06-19 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rnames_app', '0045_absoluteagevalue_historicalabsoluteagevalue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='binning',
            old_name='oldest',
            new_name='oldest_name',
        ),
        migrations.RenameField(
            model_name='binning',
            old_name='youngest',
            new_name='youngest_name',
        ),
        migrations.RenameField(
            model_name='historicalbinning',
            old_name='oldest',
            new_name='oldest_name',
        ),
        migrations.RenameField(
            model_name='historicalbinning',
            old_name='youngest',
            new_name='youngest_name',
        ),
    ]