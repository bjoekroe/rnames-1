# Generated by Django 3.2.15 on 2022-10-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rnames_app', '0050_binningabsoluteage'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrelation',
            name='database_origin',
            field=models.IntegerField(choices=[(None, '(Unknown)'), (1, 'RNames'), (2, 'Paleobiology Database'), (3, 'Macrostrat')], default=1),
        ),
        migrations.AddField(
            model_name='relation',
            name='database_origin',
            field=models.IntegerField(choices=[(None, '(Unknown)'), (1, 'RNames'), (2, 'Paleobiology Database'), (3, 'Macrostrat')], default=1),
        ),
    ]
