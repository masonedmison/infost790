"""a place to store various bookeeping stuff"""
from datetime import time

zip_sq_miles = {"53007": -1, "53202": 2, "53203": 0, "53204": 3, "53205": 1, "53206": 2, "53207": 9, "53208": 3, "53209": 10, "53210": 2, "53211": 3, "53212": 4, "53213": 3, "53214": 7, "53215": 5, "53216": 4, "53217": 13, "53218": 6, "53219": 5, "53220": 5, "53221": 8, "53222": 5, "53223": 10, "53224": 9, "53225": 6, "53226": 7, "53227": 5, "53228": 4, "53233": 1, "53235": 2, "53295": -1}

crime_type_cols = ['arson', 'assault', 'burglary', 'damage',
    'homicide', 'lv', 'robbery', 'sexoff', 'theft','cartheft']

crime_type_prett = {'arson':'Arson', 'assault':'Assualt', 'burglary':'Burglary', 'damage':'Vandalism', 'homicide':'Homicide', 'lv':'Locked Vehicle', 'robbery':'Robbery', 'sexoff':'Sexual Assualt', 'theft':'Theft','cartheft':'Car Theft'}


zip_populations = {'53007': 1841, '53202': 23386, '53203': 938, '53204': 42355, '53205': 10050, '53206': 28210, '53207': 35149, '53208': 31133, '53209': 46917, '53210': 28126, '53211': 35406, '53212': 30416, '53213': 26020, '53214': 34725, '53215': 60953, '53216': 32264, '53217': 29192, '53218': 40625, '53219': 33880, '53220': 26303, '53221': 37701, '53222': 25165, '53223': 29230, '53224': 21284, '53225': 25706, '53226': 18370, '53227': 23357, '53228': 14369, '53233': 16453, '53235': 9270, '53295': 359}

time_slots = ('12am - 8am','12am - 8am'),('8am - 4pm', '8am - 4pm'),('4pm - 12am', '4pm - 12am')

time_str_to_time = {'12am - 8am': (time(23,59), time(8,0)),'8am - 4pm':(time(8,0), time(16,0)),'4pm - 12am':(time(16,0), time(23,59))}

mke_rel_scores = {'12am - 8am': {'mean': 0.01075160756439908, 'std': 0.013216499292932579, 'max': 0.07036339563441414, 'min': 0.0}, '8am - 4pm': {'mean': 0.0124231547535046, 'std': 0.012861594974971155, 'max': 0.05970721845386047, 'min': 2.5646100872024737e-06}, '4pm - 12am': {'mean': 0.01583306394925131, 'std': 0.016314706362930333, 'max': 0.07073145175768258, 'min': 0.0}, 'all': {'mean': 0.01300260875571833, 'std': 0.014372199697976299, 'max': 0.07073145175768258, 'min': 0.0}}