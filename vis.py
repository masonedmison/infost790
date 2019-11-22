import datetime
import matplotlib.pyplot as plt
import rel_scores

#--------color bar rgba stuff--------
# cmap = plt.cm.get_cmap('viridis')

# rgba = cmap(.001, bytes=True)

# hex_c = '#{:02x}{:02x}{:02x}'.format(*rgba)
#------------------------------------
zip_ = '53211'

def create_datetime_i(df):
    """creates DatetimeIndex on passed in index"""
    dt_l = []
    for r in df.iterrows():
        dt_l.append(datetime.datetime.combine(r[1].date1, r[1].time1))
        
    df['datetime'] = dt_l
    df.set_index('datetime', inplace=True)


def extract_crimes_by_sl(df, time_sl):
    """extract crimes by a given time slot"""
    # check that index is datetime, if not make it
    create_datetime_i(df)
    return df.between_time(time_sl[0], time_sl[1])


# visualize crimes by week for zip code and time sl 
def time_sl_vis(df, z):
    """plots sum of crime weights by week for each zip_code - time slots not specified"""
    df.index = df.index.to_period('W')
    scores_ = [rel_scores.compute_crime_score(df.loc[i], z) for i in df.index.unique()]        
    x = df.index.unique().to_timestamp().values
    plt.plot(x, scores_) 
    plt.show()

res = rel_scores.query_all_crimes(zip_)
crimes = rel_scores.to_df(res)
rel_scores.create_crime_cat(crimes)
rel_scores.integrate_weight_to_df(crimes)
create_datetime_i(crimes)
print(crimes.date1.head())
time_sl_vis(crimes, zip_)
