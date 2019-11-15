"""normalize weights for crime_score"""
import numpy as np


w = {'arson':1032.275,
'assault':560.4556,
'burglary':267.8036,
'theft':12.68254,
'lv':2.833333,
'homicide':1438.667,
'sexoff':762.0163,
'damage':166.8448,
'cartheft':36.96875}

max_ = 1438.667
min_ = 2.833
mean_ = np.sum(list(w.values()))/len(w.values())


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
