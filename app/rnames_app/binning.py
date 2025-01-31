from .utils.info import BinningProgressUpdater
from .utils.root_binning_ids import main_binning_fun
from . import models
import traceback

from django.db import connection
from types import SimpleNamespace

import pandas as pd

def get_table_as_df(db_columns, model):
    queryset_list = list(model.objects.select_related().values_list(*db_columns))
    df = pd.DataFrame(queryset_list)
    columns = []

    for col in db_columns:
        columns.append(col.replace('__', '_'))

    df.columns = columns
    return df

def get_relations_df():
    db_columns = [
        'id',
        'reference__id',
        'reference__title',
        'reference__year',


        'name_one__id',
        'name_one__location__name',
        'name_one__name__name',
        'name_one__qualifier__level',
        'name_one__qualifier__qualifier_name__name',
        'name_one__qualifier__stratigraphic_qualifier__name',
        'name_one__remarks',

        'name_two__id',
        'name_two__location__name',
        'name_two__name__name',
        'name_two__qualifier__level',
        'name_two__qualifier__qualifier_name__name',
        'name_two__qualifier__stratigraphic_qualifier__name',
        'name_two__remarks',

        'database_origin',
    ]

    return get_table_as_df(db_columns, models.Relation)

def get_structured_names_df():
    db_columns = [
        'id',

        'name__name',
        'location__name',

        'qualifier__qualifier_name__name',
        'qualifier__stratigraphic_qualifier__name',
        'qualifier__level',

        'reference__id',
        'reference__first_author',
        'reference__year',
        'reference__title',
    ]

    return get_table_as_df(db_columns, models.StructuredName)

def process_binning_result(scheme_id, df, info = None):
    scheme = models.TimeScale.objects.get(pk=scheme_id)
    create_objects = []

    print('Processing binning result')

    models.Binning.objects.filter(binning_scheme=scheme_id).delete()

    col = SimpleNamespace(**{k: v for v, k in enumerate(df.columns)})

    for row in df.values:
        obj = models.Binning(refs=row[col.refs], binning_scheme=scheme)
        obj.structured_name_id = structured_name=row[col.name_id]
        obj.youngest_id = youngest=row[col.youngest_id]
        obj.oldest_id = oldest=row[col.oldest_id]

        create_objects.append(obj)

    models.Binning.objects.bulk_create(create_objects, 100)
    # info.finish_binning()

def process_binning_absolute_age_result(scheme_id, df, info = None):
    scheme = models.TimeScale.objects.get(pk=scheme_id)
    create_objects = []

    print('Processing binning result')

    models.BinningAbsoluteAge.objects.filter(binning_scheme=scheme_id).delete()

    col = SimpleNamespace(**{k: v for v, k in enumerate(df.columns)})

    for row in df.values:
        obj = models.BinningAbsoluteAge(refs=row[col.refs], binning_scheme=scheme, oldest_age=row[col.oldest_age],
            youngest_age=row[col.youngest_age], reference_age=row[col.ref_age], age_constraints=row[col.age_constraints])
        obj.structured_name_id = structured_name=row[col.name_id]
        obj.youngest_id = youngest=row[col.youngest_id]
        obj.oldest_id = oldest=row[col.oldest_id]

        create_objects.append(obj)

    models.BinningAbsoluteAge.objects.bulk_create(create_objects, 100)
    # info.finish_binning()

def binning_process(scheme_id):
    connection.connect()
    # info = BinningProgressUpdater()

    # if not info.start_binning():
    #     return

    pd.set_option('display.max_columns', None)

    relations = get_relations_df()
    print(relations)

    structured_names = get_structured_names_df()
    print(structured_names)

    time_scale = pd.DataFrame(list(models.TimeScale.objects.filter(pk=scheme_id).values('id', 'ts_name')))
    sequence = pd.DataFrame(list(models.BinningSchemeName.objects.filter(ts_name=scheme_id).order_by('sequence').values('id', 'ts_name', 'structured_name', 'sequence')))
    sequence.rename(inplace=True, columns={'ts_name': 'ts_name_id', 'structured_name': 'structured_name_id'})

    print('Binning ' + time_scale['ts_name'][0])

    try:
        result = main_binning_fun(time_scale['ts_name'][0], time_scale, sequence, relations, structured_names)
    except:
        traceback.print_exc()
        return

    # print(result['binning'].columns)
    # Index(['name_id', 'name', 'qualifier_name', 'oldest_id', 'oldest_name', 'youngest_id', 'youngest_name', 'refs', 'binning_scheme'], dtype='object')
    print(result['binning'])

    # print(result['generalised'].columns)
    # Index(['name', 'oldest', 'youngest', 'binning_scheme'], dtype='object')
    print(result['generalised'])

    # print(result['absolute_ages'].columns)
    # Index(['name_id', 'name', 'qualifier_name', 'oldest_id', 'oldest_name', 'youngest_id', 'youngest_name', 'refs', 'binning_scheme', 'oldest_age', 'youngest_age', 'ref_age', 'age_constraints'], dtype='object')
    print(result['absolute_ages'])

    process_binning_result(scheme_id, result['binning'])
    process_binning_absolute_age_result(scheme_id, result['absolute_ages'])
    print('Binning finished')
