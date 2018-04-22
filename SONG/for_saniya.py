#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import glob
from  os.path import expanduser
import os
import pandas as pd
import sys

song=pd.read_csv('param_input_and_out.csv')
host=song[song['label']=='host']
field=song[song['label']=='field']

song=song[['HIP', 'MH', 'eMH', 'Teff', 'eTeff', 'logg_x', 'elogg', 'L', 'eL', 'label']]
song['Notes']='SONG'
song.rename(columns = {'logg_x':'logg','L':'L_hip'}, inplace = True)
song.to_csv('song_survey_hip_L.csv',index=False)
