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

xhip=pd.read_csv(home+'/Dropbox/PhD/XHIPforTom.csv')#entire HIP catalog
#'HIP,ra,dec,parallax,err(parallax),V,I,B-V,err(B-V),teff,lum,rad,numax'

xhip['Mv']=xhip['V']+5*np.log10(xhip['parallax']/100)
#johnson2006 criteria 0.5<MV<3.5, 0.55<B-V<1.0, and V <=7.6
#witt11 1.0 < (B-V ) < 1.2, 1.8 < MV < 3.0, and V < 8.0.

xhip=xhip[(0.55<xhip['B-V']) & (xhip['B-V']<1.2) & (0.5<xhip['Mv']) & (xhip['Mv']<3.5)]

xhip['V']=pd.to_numeric(xhip['V'],errors='coerce')

xhip.sort_values(by=['dec'],inplace=True)
xhip.reset_index(inplace=True,drop=True)
#xhip.to_csv('check_with_K2fov8.csv',columns=['ra','dec','st_optmag'],header=None,index=False)
#subprocess.call(['K2findCampaigns-csv', 'check_with_K2fov8.csv'])


camp=pd.read_csv('xhip_check_with_K2fov.csv-K2findCampaigns.csv',header=None,names=['RA','Dec','V','Camp'])
camp8=pd.read_csv('xhip_check_with_K2fov8.csv-K2findCampaigns.csv',header=None,names=['RA','Dec','V','Camp'])
camp2=pd.read_csv('xhip_check_with_K2fov2.csv-K2findCampaigns.csv',header=None,names=['RA','Dec','V','Camp'])
camp=pd.concat([camp,camp8])
camp.reset_index(inplace=True,drop=True)
camp=pd.concat([camp,camp2])
camp.sort_values(by=['Dec'],inplace=True)
camp.reset_index(inplace=True,drop=True)

camp['Camp']=camp['Camp'].str.replace('[','')
camp['Camp']=camp['Camp'].str.replace(']','')
camp['Camp']=pd.to_numeric(camp['Camp'],errors='coerce')
camp['V']=pd.to_numeric(camp['V'],errors='coerce')

xhip=pd.concat([xhip,camp],axis=1)

xhip.dropna(subset=['Camp'],inplace=True)
xhip.reset_index(inplace=True,drop=True)
print(xhip)

hip_hd=pd.read_csv(home+'/Dropbox/PhD/Year_4/Porto/Literature_Values_Mass_etc/hip_hd.tsv',comment='#',sep='\t',usecols=('HD','HIP'))
#HIP and HD catalog numbers
print(len(xhip))
xhip=pd.merge(left=xhip,left_on='HIP',right=hip_hd,right_on='HIP',how='left')
print(len(xhip))
