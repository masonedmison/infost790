"""a place for querying and processing or the stuff that creates the score shown on in the user table"""
import json
import pandas as pd
from app import cursor # cursor object to execute queries
from processing import static_computations 
from mappings import (zip_sq_miles, crime_type_cols, crime_type_prett, zip_populations)

# ----------------Queries-------------------
def query_all_crimes(zip_):
    """get all crimes by zip from crime table"""
    q_str = f"""SELECT * FROM "Crime" WHERE zip={zip_} ;"""
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

# ------------------------------------------------

# -------------driver methods-------------------
def generate_stats(zip_):
    """takes a zip code and generates relevant stats using other methods in this module"""
    stats =[]
    res = query_all_crimes(zip_)
    crimes = to_df(res)
    # add recode cols
    create_crime_cat(crimes) 
    integrate_weight_to_df(crimes)
    ####
    # gets various scores
    most_comm_crime = get_most_common_crime(crimes)
    crimes_per_sq_mile = crimes_per_square_mile(crimes, zip_)
    cas = compute_crime_score(crimes, zip_)  
    ####
    # build crime statistics dictionary
    stats.append(dict(name='Crime Assessment Score', score = cas))  # crime assessment score
    stats.append(dict(name='Most Common Crime', score = crime_type_prett[most_comm_crime]))  # most common crime
    stats.append(dict(name='Crimes Per Square Mile', score = crimes_per_sq_mile))  # most common crime
    return stats
    ####
