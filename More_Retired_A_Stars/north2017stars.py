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

north=pd.read_csv('North2017_spec_params.csv')
north['espec_feh']=np.sqrt(north['espec_feh']**2 + 0.062**2)#add torres bit
north['espec_feh'][north['espec_feh']<0.1]=0.1


north[['mDnu', 'emDnu', 'mnumax', 'emnumax', 'Teff', 'eTeff']]=north[['mDnu', 'emDnu', 'mnumax', 'emnumax', 'Teff', 'eTeff']].round(1)
north[['spec_logg', 'espec_logg', 'spec_feh', 'espec_feh']]=north[['spec_logg', 'espec_logg', 'spec_feh', 'espec_feh']].round(2)
hip_hd=pd.read_csv('hip_hd.tsv',comment='#',sep='\t',usecols=('HD','HIP'))
north=pd.merge(left=north,left_on='HD',right=hip_hd,right_on='HD',how='left')
north.rename(columns = {'Source':'Notes'}, inplace = True)
north['HIP']='HIP'+north['HIP'].astype(int).astype(str)
north[['HIP','HD','Teff', 'eTeff', 'spec_logg', 'espec_logg', 'spec_feh', 'espec_feh','Notes']].to_csv('North2017RetAstars.csv',index=False)
print(north)
