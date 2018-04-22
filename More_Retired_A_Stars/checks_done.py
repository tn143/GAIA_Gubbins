from __future__ import print_function,division
import os
from os.path import expanduser
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import fnmatch
import pandas as pd
import subprocess


home=expanduser('~')

#xhip=pd.read_csv(home+'/Dropbox/PhD/XHIPforTom.csv')#entire HIP catalog
#'HIP', 'ra', 'dec', 'parallax', 'err(parallax)', 'V', 'I', 'B-V', 'err(B-V)', 'teff', 'lum', 'rad', 'numax', 'Mv',
#'RA', 'Dec', 'V.1', 'Camp', 'HD'
#johnson2006 criteria 0.5<MV<3.5, 0.55<B-V<1.0, and V <=7.6
#witt11 1.0 < (B-V ) < 1.2, 1.8 < MV < 3.0, and V < 8.0.
#xhip=xhip[(0.55<xhip['B-V']) & (xhip['B-V']<1.2) & (0.5<xhip['Mv']) & (xhip['Mv']<3.5)]
'''
xhip=pd.read_csv('checksdone.csv')
hosts=pd.read_csv('tastyhosts.csv')
#hosts['hd_name']=hosts['hd_name'].str.replace('HD','').astype(int)
hosts['hip_name']=hosts['hip_name'].str.replace('HIP|A|B','').astype(int)
xhip['label']='field'
xhip['label'][xhip['HIP'].isin(hosts['hip_name'])]='host'
xhip['HIP']='HIP'+xhip['HIP'].astype(int).astype(str)
epic=pd.read_csv('epic_details.txt',sep='\t',comment='#')
xhip.sort_values(by='ra',inplace=True)
xhip.reset_index(inplace=True,drop=True)
epic.sort_values(by='RA',inplace=True)
epic.reset_index(inplace=True,drop=True)

all=pd.concat([xhip,epic],axis=1)
all.reset_index(inplace=True,drop=True)
all.to_csv('ALL.csv',index=False)
'''
all=pd.read_csv('all.csv')
print(list(all))
all['Notes']='EPIC'

print(list(all))
print(all[['HIP','HD','Teff', 'ep_teff', 'em_teff', 'logg', 'ep_logg', 'em_logg', '[Fe/H]', 'ep_[Fe/H]', 'em_[Fe/H]']][all['label']=='host'])

all[['HIP','HD','Teff', 'ep_teff', 'em_teff', 'logg', 'ep_logg', 'em_logg', '[Fe/H]', 'ep_[Fe/H]', 'em_[Fe/H]','Notes']].to_csv('saniya_retired_A_stars.csv',index=False)
