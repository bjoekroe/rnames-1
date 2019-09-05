# Generated by Django 2.0.9 on 2019-01-17 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mb', '0013_auto_20190117_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('choice_set', models.CharField(help_text='Enter the Choice Set of the ChoiceValue', max_length=25)),
                ('caption', models.CharField(help_text='Enter the Caption of the ChoiceValue', max_length=25)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdby_choicevalue', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiedby_choicevalue', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'ordering': ['caption'],
            },
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('name', models.CharField(help_text='Enter the Name of the FoodItem', max_length=250)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdby_fooditem', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiedby_fooditem', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalChoiceValue',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('modified_on', models.DateTimeField(blank=True, editable=False)),
                ('history_change_reason', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('choice_set', models.CharField(help_text='Enter the Choice Set of the ChoiceValue', max_length=25)),
                ('caption', models.CharField(help_text='Enter the Caption of the ChoiceValue', max_length=25)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'verbose_name': 'historical choice value',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFoodItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('modified_on', models.DateTimeField(blank=True, editable=False)),
                ('history_change_reason', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Is the record active')),
                ('name', models.CharField(help_text='Enter the Name of the FoodItem', max_length=250)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='The user that is automatically assigned')),
            ],
            options={
                'verbose_name': 'historical food item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
