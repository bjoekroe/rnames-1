# Generated by Django 3.2.15 on 2022-09-16 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rnames_app', '0046_auto_20220619_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binning',
            name='name',
        ),
        migrations.RemoveField(
            model_name='binning',
            name='oldest_name',
        ),
        migrations.RemoveField(
            model_name='binning',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='binning',
            name='ts_count',
        ),
        migrations.RemoveField(
            model_name='binning',
            name='youngest_name',
        ),
        migrations.RemoveField(
            model_name='historicalbinning',
            name='name',
        ),
        migrations.RemoveField(
            model_name='historicalbinning',
            name='oldest_name',
        ),
        migrations.RemoveField(
            model_name='historicalbinning',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='historicalbinning',
            name='ts_count',
        ),
        migrations.RemoveField(
            model_name='historicalbinning',
            name='youngest_name',
        ),
        migrations.AddField(
            model_name='binning',
            name='oldest',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='oldest', to='rnames_app.structuredname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binning',
            name='structured_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='structured_name', to='rnames_app.structuredname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binning',
            name='youngest',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='youngest', to='rnames_app.structuredname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalbinning',
            name='oldest',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rnames_app.structuredname'),
        ),
        migrations.AddField(
            model_name='historicalbinning',
            name='structured_name',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rnames_app.structuredname'),
        ),
        migrations.AddField(
            model_name='historicalbinning',
            name='youngest',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rnames_app.structuredname'),
        ),
    ]
