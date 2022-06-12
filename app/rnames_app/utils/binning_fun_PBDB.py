#!/usr/bin/env python
# coding: utf-8

import pandas as pd


###################
# many PBDB structured names refer to absolute ages 
# these ages are coherent with in PBDB but not with other ages from e.g. younger publications
# to use PBDB age grouping a special binning algorithm is needed
# bin_fun_PBDB is doing this.
#

def bin_fun_PBDB (c_rels, c_strat, binning_scheme, ts_names, t_scales):
    
    t_scheme = binning_scheme
    x_names = ts_names[ts_names['ts_name']==t_scheme]
    used_ts = t_scales[t_scales['ts_name_id']==x_names['id'].values[0]]
    # rename columns in order to make compatible with following code
    used_ts = used_ts[['structured_name_id', 'sequence']]
    used_ts.rename(columns={'structured_name_id':'ts', 'sequence': 'ts_index'},inplace = True)

    PBDB_id = c_rels.loc[(c_rels["reference_title"]=="Paleobiology Database"),["reference_id"]]
    PBDB_id = PBDB_id.drop_duplicates()

    c_rels = c_rels[['id', 'name_one_id', 'name_two_id','name_one_qualifier_stratigraphic_qualifier_name', 
                              'name_two_qualifier_stratigraphic_qualifier_name', 'reference_id', 'reference_year']]
    c_rels.rename(columns={'name_one_id': 'name_1', 'name_two_id':'name_2', 
                         'name_one_qualifier_stratigraphic_qualifier_name': 'strat_qualifier_1',
                         'name_two_qualifier_stratigraphic_qualifier_name': 'strat_qualifier_2'},inplace = True) # rename to fit following code
    # make c_rels two-sided
    c_relsx = c_rels[['id', 'name_2','strat_qualifier_2','name_1', 'strat_qualifier_1', 'reference_id', 'reference_year']]
    c_relsx.columns = ['id', 'name_1','strat_qualifier_1','name_2', 'strat_qualifier_2','reference_id', 'reference_year']
    c_rels = pd.concat([c_rels.reset_index(drop=False), c_relsx.reset_index(drop=False)], axis=0)
    c_rels = c_rels.reset_index(drop=True)
    
    # get absolute ages of ts from pbdb    
    c_rels_abs_ts = c_rels[c_rels['name_1'].isin(used_ts['ts'])]
    c_rels_abs_ts = c_rels_abs_ts[(c_rels_abs_ts['strat_qualifier_2']=='Absolute age')] # all absolute ages of ts

    abs_ages = c_strat[(c_strat['qualifier_qualifier_name_name']=='mya') &
                         (c_strat['remarks']=='Autogenerated by PBDB importer.')]
    abs_ages = abs_ages[['id','name_name']]
    abs_ages['name_name'] = pd.to_numeric(abs_ages['name_name'])
    abs_ts = pd.merge(c_rels_abs_ts, abs_ages, how= 'inner', left_on="name_2", right_on="id")
    abs_ts = pd.merge(c_rels_abs_ts, abs_ages, how= 'inner', left_on="name_2", right_on="id")

    PBDB_ts_binned = pd.DataFrame([] * 6, columns=['name', 'oldest','youngest', 'ts_count', 'refs', 'rule'])
    PBDB_ts_binned_abs = pd.DataFrame([] * 6, columns=['name', 'oldest','youngest', 'ts_count', 'refs', 'rule'])
    for i in range(0,len(used_ts)):
        x_abs_ts = abs_ts[abs_ts['name_1'] == used_ts['ts'].iloc[i]]
        if x_abs_ts.shape[0]>0:
            oldest = max(pd.to_numeric(x_abs_ts['name_name']))
            youngest = min(pd.to_numeric(x_abs_ts['name_name']))
            x_youngest = x_abs_ts[x_abs_ts['name_name'] == youngest]
            x_oldest = x_abs_ts[x_abs_ts['name_name'] == oldest]
            combi = pd.DataFrame([{'name': x_abs_ts['name_1'].iloc[0],
                               'oldest': x_oldest['id_x'].iloc[0], 'youngest': x_youngest['id_x'].iloc[0],
                               'ts_count': 0,'refs':PBDB_id['reference_id'].iloc[0], 'rule': 7.0}])
            combi_abs = pd.DataFrame([{'name': x_abs_ts['name_1'].iloc[0],
                               'oldest': oldest, 'youngest': youngest,
                               'ts_count': 0,'refs':PBDB_id['reference_id'].iloc[0], 'rule': 7.0}])
            PBDB_ts_binned = pd.concat([PBDB_ts_binned, combi], axis=0)
            PBDB_ts_binned_abs = pd.concat([PBDB_ts_binned_abs, combi_abs], axis=0)
        
    combi = pd.DataFrame([{'name': x_abs_ts['name_1'].iloc[0],
                       'oldest': x_oldest['id_x'].iloc[0], 'youngest': x_youngest['id_x'].iloc[0],
                       'ts_count': 0,'refs':PBDB_id['reference_id'].iloc[0], 'rule': 7.0}])
    combi_abs = pd.DataFrame([{'name': x_abs_ts['name_1'].iloc[0],
                       'oldest': oldest, 'youngest': youngest,
                       'ts_count': 0,'refs':PBDB_id['reference_id'].iloc[0], 'rule': 7.0}])
    PBDB_ts_binned = pd.concat([PBDB_ts_binned, combi], axis=0)
    PBDB_ts_binned_abs = pd.concat([PBDB_ts_binned_abs, combi_abs], axis=0)

    # all other absolute ages from pbdb
    c_rels_abs = c_rels[(c_rels['strat_qualifier_2']=='Absolute age')]
    c_rels_abs = pd.merge(c_rels_abs, abs_ages, how= 'inner', left_on="name_2", right_on="id")
    c_rels_abs = c_rels_abs[c_rels_abs['reference_id'] == PBDB_id['reference_id'].iloc[0]]

    names_with_PBDB_age = c_rels_abs['name_1'].drop_duplicates()
    names_with_PBDB_age = names_with_PBDB_age.to_frame()

    PBDB_names_binned = pd.DataFrame([] * 6, columns=['name', 'oldest','youngest', 'ts_count', 'refs', 'rule'])
    for i in range(0,len(names_with_PBDB_age)):
        x_c_rels_abs = c_rels_abs[c_rels_abs['name_1'] == names_with_PBDB_age['name_1'].iloc[i]]
        if x_c_rels_abs.shape[0]>0:
            oldest = max(pd.to_numeric(x_c_rels_abs['name_name']))   
            youngest = min(pd.to_numeric(x_c_rels_abs['name_name']))
            x_strat_oldest = PBDB_ts_binned_abs[(PBDB_ts_binned_abs['youngest']<=oldest) & (PBDB_ts_binned_abs['oldest']>=oldest)]
            x_strat_youngest = PBDB_ts_binned_abs[(PBDB_ts_binned_abs['youngest']<=youngest) & (PBDB_ts_binned_abs['oldest']>=youngest)]
            if (x_strat_oldest.shape[0]>0) & (x_strat_youngest.shape[0]>0):
                yts = used_ts[used_ts['ts']==x_strat_youngest['name'].iloc[0]]
                ots = used_ts[used_ts['ts']==x_strat_oldest['name'].iloc[0]]
                combi = pd.DataFrame([{'name': names_with_PBDB_age['name_1'].iloc[i],
                                   'oldest': x_strat_oldest['name'].iloc[0], 'youngest': x_strat_youngest['name'].iloc[0],
                                   'ts_count': yts['ts_index'].iloc[0]-ots['ts_index'].iloc[0],
                                   'refs':PBDB_id['reference_id'].iloc[0], 'rule': 7.1}])
                PBDB_names_binned = pd.concat([PBDB_names_binned, combi], axis=0)
    return PBDB_names_binned  