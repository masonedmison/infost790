"""a place for querying and processing or the stuff that creates the score shown on in the user table"""
import json
import datetime
import pandas as pd
from app import cursor # cursor object to execute queries
import static_computations 
from mappings import (zip_sq_miles, crime_type_cols, crime_type_prett, zip_populations, time_str_to_time, mke_rel_scores)

# ----------------Queries-------------------
def query_all_crimes(zip_= None):
    """get all crimes by zip from crime table"""
    if zip_ is not None:
        q_str = f"""SELECT * FROM "Crime" WHERE zip={zip_} ;"""
    else:  # else get all the data 
        q_str = f"""SELECT * FROM "Crime"  ;"""
    cursor.execute(q_str)
    return cursor.fetchall()
# -----------------------------------------

# -----------Computations---------------
def get_most_common_crime(res):
   """get most common crime"""
   return res.CrimeType.value_counts().index[0]


def crimes_per_square_mile(df, zip_):
    """Crimes per square mile"""
    if zip_ not in zip_sq_miles.keys():
        return -1
    zip_sq = zip_sq_miles[zip_]
    return len(df)/ zip_sq


def compute_crime_score(df, zip_):
    """compute crime score"""
    z_pop = zip_populations[zip_]
    return df.CrimeWeight.sum()/ z_pop


def crime_score_bdown(com_crime):
    """create breakdown of crime score
    Returns:
        str of crime score breakdown (most common crime and crime per 1000)
    """
    pass


def calc_percentile(i_score, zip_, df):
    zips_to_calc = set(zip_populations.keys())
    zips_to_calc.remove(zip_)  # remove zip to get percentile for
    count = 0
    for z in zips_to_calc:
        s = compute_crime_score(df, z)
        if s <= i_score:
            count += 1
    return 100.0 * count / len(zips_to_calc)

def min_max_normalization(score_, time_sl):
    max_ = mke_rel_scores[time_sl]['max']
    min_ = mke_rel_scores[time_sl]['min']
    return (score_-min_)/(max_- min_)
# -------------------------------------------

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

# ------------------------------------------------

# -------------driver methods-------------------
def generate_stats(zip_, time_sl):
    """takes a zip code and generates relevant stats using other methods in this module"""
    stats =[]
    res = query_all_crimes(zip_=zip_)
    crimes = to_df(res)
    # extract relevant crimes by time slot
    time_obj = time_str_to_time[time_sl]  # time span to find all crimes within 
    crimes = extract_crimes_by_sl(crimes, time_obj)
    crimes.reset_index(inplace=True) 
    ####
    # add recode cols
    create_crime_cat(crimes) 
    integrate_weight_to_df(crimes)
    ####
    # gets various scores
    most_comm_crime = get_most_common_crime(crimes)
    # crimes_per_sq_mile = crimes_per_square_mile(crimes, zip_)
    cas = compute_crime_score(crimes, zip_)  
    norm_cas = min_max_normalization(cas, time_sl)
    ####
    # build crime statistics dictionary
    stats.append(dict(name='Crime Assessment Score', score = round(norm_cas*100, 2) ))  # crime assessment score
    stats.append(dict(name='Most Common Crime', score = crime_type_prett[most_comm_crime]))  # most common crime
    # stats.append(dict(name='Crimes Per Square Mile', score = crimes_per_sq_mile))  # most common crime
    return stats
    ####
