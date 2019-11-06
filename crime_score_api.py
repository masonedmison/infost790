"""a place for querying and processing"""
import json
import pandas as pd
from app import cursor # cursor object to execute queries


# crime score api
ZIP_CODE_SQ = json.load(open('processing/mappings/zip_square_miles.json'))
CRIME_TYPE_COLS = ['arson', 'assault', 'burglary', 'damage',
    'homicide', 'lv', 'robbery', 'sexoff', 'theft','cartheft']


# ----------------Queries-------------------
def query_all_crimes(zip):
    """get all crimes by zip from crime table"""
    q_str = f"""SELECT * FROM "Crime" WHERE zip={zip} ;"""
    cursor.execute(q_str)
    return cursor.fetchall()
# -----------------------------------------

# -----------Data Extraction ---------------
def get_most_common_crime(res):
   """get most common crime"""
   return res.CrimeType.value_counts().index[0]


def crimes_per_square_mile(df, zip_):
    """Crimes per square mile"""
    if zip_ not in ZIP_CODE_SQ.keys():
        return -1
    zip_sq = ZIP_CODE_SQ[zip_]
    return len(df)/ zip_sq


def get_time_span(res):
    pass
# -------------------------------------------

# -------------Pandas functions-----------------
def create_crime_cat(df):
    """Creates CrimeType column and populates based off boolean values in CRIME TYPE COLUMNS"""
    df['CrimeType'] = ''
    for ct in CRIME_TYPE_COLS:
        c_int = df[ct].astype('int32')
        sub = c_int[c_int == 1] 
        df.CrimeType.iloc[sub.index] = ct


def to_df(res):
    return pd.DataFrame(data=res, columns=[x[0] for x in cursor.description])

# ------------------------------------------------

# -------------driver methods-------------------
def generate_stats(zip_):
    """takes a zip code and generates relevant stats using other methods in this module"""
    stats =[]
    res = query_all_crimes(zip_)
    crimes = to_df(res)
    create_crime_cat(crimes)  # creates crime category in place
    most_comm_crime = get_most_common_crime(crimes)
    crimes_per_sq_mile = crimes_per_square_mile(crimes, zip_)

    ####
    # build crime statistics dictionary
    stats.append(dict(name='Common Crime', score = most_comm_crime))  # most common crime
    stats.append(dict(name='Crimes per Square Mile', score = crimes_per_sq_mile))  # Crimes per square mile

    return stats
    ####
