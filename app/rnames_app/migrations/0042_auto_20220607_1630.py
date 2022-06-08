# Generated by Django 3.2.13 on 2022-06-07 13:30

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rnames_app', '0041_timescale'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaltimescale',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical time scale'},
        ),
        migrations.AlterField(
            model_name='timescale',
            name='created_by',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdby_timescale', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned'),
        ),
        migrations.AlterField(
            model_name='timescale',
            name='modified_by',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiedby_timescale', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned'),
        ),
    ]