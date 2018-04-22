#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,division
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from os.path import expanduser
import sys
import pandas as pd
import os

home=expanduser('~')
def numax(logg,teff):
	g=(10**logg)/100.
	nu=3150*(g/274.)*(teff/5777.)**-0.5
	return nu



koi6194=pd.read_csv('koi6194.in',delim_whitespace=True)
koi6194=koi6194[['#KIC','MH', 'eMH', 'Teff', 'eTeff', 'logg', 'elogg']]
koi6194.rename(columns={'#KIC':'ID'},inplace=True)
koi6194['Notes']='apokasc DR13, MH is feh'

koi3890=pd.read_csv('3890_dp.in',delim_whitespace=True)
koi3890=koi3890[['ID','feh', 'efeh', 'teff', 'eteff', 'logg', 'elogg']]
koi3890.rename(columns={'feh':'MH', 'efeh':'eMH', 'teff':'Teff', 'eteff':'eTeff'},inplace=True)
koi3890=koi3890.iloc[-1:,]
koi3890['logg']=2.92
koi3890['elogg']=0.1
koi3890['ID']='koi3890'
koi3890['Notes']='SPC with seismic logg prior'

kois=pd.concat([koi6194,koi3890])
kois.to_csv('interestingKOIs.csv',index=False)

print(kois)
