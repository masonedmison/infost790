"""a script to gather average Crime Assesment Scores for Milwaukee - only needs run once. Resulting Scores are stored in mappings.py as mke_rel_scores"""
import numpy as np
import psycopg2
import pandas as pd
import datetime
from config import Config
import static_computations
from mappings import (crime_type_cols, time_slots, zip_populations, time_str_to_time)

# db stuff
conn = psycopg2.connect(dbname=Config.dbname, user=Config.user, host=Config.host, password=Config.password)
cursor = conn.cursor()
####

#----- fetch and extraction-----
def query_all_crimes(zip_):
    """get all crimes by zip from crime table"""
    q_str = f"""SELECT * FROM "Crime" WHERE zip={zip_} ;"""
    cursor.execute(q_str)
    return cursor.fetchall()


# -------------Pandas functions-----------------
def create_crime_cat(df):
    """Creates CrimeType column and populates based off boolean values in CRIME TYPE COLUMNS"""
    df['CrimeType'] = ''
    for ct in crime_type_cols:
        c_int = df[ct].astype('int32')
        sub = c_int[c_int == 1]
        df.CrimeType.iloc[sub.index] = ct


def to_df(res):
    return pd.DataFrame(data=res, columns=[x[0] for x in cursor.description])


def integrate_weight_to_df(df):
    """create CrimeWeight columnm using max-min normalized values from Cambridge Average Harm Index"""
    w = static_computations.max_min_norm()
    df['CrimeWeight'] = float(0) 
    for k,v in w.items():
        sub = df[df.CrimeType==k]
        df.CrimeWeight[sub.index] = v

def extract_crimes_by_sl(df, time_sl):
    """extract crimes by a given time slot"""
    dt_l = []
    for r in df.iterrows():
        dt_l.append(datetime.datetime.combine(r[1].date1, r[1].time1))
        
    df['datetime'] = dt_l
    df.set_index('datetime', inplace=True)
    return df.between_time(time_sl[0], time_sl[1])

# ----------------------------------------------

#---------computations-----------
def compute_crime_score(df, zip_):
    """compute crime score"""
    z_pop = zip_populations[zip_]
    return df.CrimeWeight.sum()/ z_pop
#--------------------------------

def get_mke_scores():
    """get descriptive stats for all mke zips for all time slots"""
    _scores = {k:[] for k in time_str_to_time.keys()} 
    _scores['all'] = []  # add key for all milwaukee and all time zones
    for zip_ in zip_populations.keys(): 
        res = query_all_crimes(zip_=zip_)
        print(f'[PROCESSING] {zip_}')
        crimes = to_df(res)
        create_crime_cat(crimes)
        integrate_weight_to_df(crimes)
        for time_sl in time_str_to_time.keys():
           sub = extract_crimes_by_sl(crimes, time_str_to_time[time_sl]) 
           cas = compute_crime_score(sub, zip_) 
           _scores[time_sl].append(cas)
           _scores['all'].append(cas)
    return _scores


def compute_desc_stats(score_d):
    """takes dict where values are lists - iters through list and computes descriptive stats
    returns dict with descriptive stats"""
    _scores = {k:{} for k in time_str_to_time.keys()} 
    _scores['all'] = {}  # add key for all milwaukee and all time zones
    for d in score_d: 
        mean = np.mean(score_d[d])
        std = np.std(score_d[d])
        _scores[d]['mean'] = mean
        _scores[d]['std'] = std
        _scores[d]['max'] = max(score_d[d])
        _scores[d]['min'] = min(score_d[d])
            
    return _scores


def display_mke_desc_stats():
    all_scores = get_mke_scores()
    desc_stats = compute_desc_stats(all_scores)
    print(desc_stats)


if __name__ == '__main__':
    display_mke_desc_stats()