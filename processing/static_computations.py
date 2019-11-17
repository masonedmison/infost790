"""normalize weights for crime_score"""
from statistics import mean
import numpy as np
from mappings import time_slots

# Weights as given in the Cambridge Harm Index
w = {'arson':1032.275,
'assault':560.4556,
'burglary':267.8036,
'theft':12.68254,
'lv':2.833333,
'homicide':1438.667,
'sexoff':762.0163,
'damage':166.8448,
'cartheft':36.96875}

max_ = max(list(w.values()))
min_ = min(list(w.values())) 
mean_ = np.sum(list(w.values()))/len(w.values())

# ---------normazlization stuff-----------
def max_min_norm():
    """normalize values of crime weight dict_"""
    dict_ = w.copy()
    for k, v in dict_.items():
        norm_v = float((v-min_)/(max_-min_))
        dict_[k] = norm_v
    return dict_


def mean_norm():
    """compute mean-norm of vaues in dictionary"""
    dict_ = w.copy()
    for k,v in dict_.items():
        m_norm = float((v-mean_)/(max_-min_))
        dict_[k] = m_norm
    return dict_
# --------------------------------------

# -------miscellaneous computations---------
def extract_time_slot(df):
    """extract all crimes that happen within a 'time_slot'"""
    pass


def get_relative_crime_scores(df):
    """compute relative crime scores for all of Milwaukee for each timeslot option"""
    pass