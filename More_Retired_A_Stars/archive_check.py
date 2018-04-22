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



conf=pd.read_csv('conf_all_all_21418.csv',comment='#')
conf=conf[conf['pl_discmethod']=='Radial Velocity']
conf.drop_duplicates(['pl_hostname'],inplace=True)
#conf['hip_name']=conf['hip_name'].str.replace('HIP|A|B','').astype(int)
#conf['hd_name']=conf['hd_name'].str.replace('HD','').astype(int)
conf=conf[(0.55<conf['st_bmvj']) & (conf['st_bmvj']<1.2)]

conf['gaia_plx']=conf['gaia_plx'].astype(float)
conf['plx']=conf['st_plx']
conf['V']=conf['st_vj'].astype(float)

conf['Mv']=conf['V']+5*np.log10(conf['plx']/100)
conf['Mv_g']=conf['V']+5*np.log10(conf['gaia_plx']/100)
conf=conf[((0.5<conf['Mv']) & (conf['Mv']<3.5)) | ((0.5<conf['Mv_g']) & (conf['Mv_g']<3.5))]
conf.reset_index(inplace=True,drop=True)
print(conf[['pl_hostname','hip_name','ra','dec','Mv','Mv_g']])
#conf.to_csv('check_with_K2fov.csv',columns=['ra','dec','st_optmag'],header=None,index=False)
#subprocess.call(['K2findCampaigns-csv', 'check_with_K2fov.csv'])
camp=pd.read_csv('check_with_K2fov.csv-K2findCampaigns.csv',header=None,names=['RA','Dec','V','Camp'])
print(camp)
camp['Camp']=camp['Camp'].str.replace('[','')
camp['Camp']=camp['Camp'].str.replace(']','')
camp['Camp']=pd.to_numeric(camp['Camp'],errors='coerce')
conf=pd.concat([conf,camp],axis=1)

conf.dropna(subset=['Camp'],inplace=True)
conf.reset_index(inplace=True,drop=True)
conf.to_csv('tastyhosts.csv',index=False)

print(conf[['pl_hostname','hip_name','ra','dec','Mv','Mv_g','Camp']])
