#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function,division

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from astropy.coordinates import SkyCoord
import astropy.units as units
from dustmaps.bayestar import BayestarQuery
from dustmaps.bayestar import BayestarWebQuery

def bolcorr(teff,eteff):#torres relations
	lteff=np.log10(teff)

	BCv = (-0.190537291496456*10.0**5) + (0.155144866764412*10.0**5*lteff) + (-0.421278819301717*10.0**4.0*lteff**2.0) + (0.381476328422343*10.0**3*lteff**3.0)
	#eBCv= (0.155144866764412*10.0**5 * eteff/(teff*np.log(10)))


	BCv[(3.70 <lteff) & (lteff<3.90)] = (-0.370510203809015*10.0**5) + (0.385672629965804*10.0**5*lteff[(3.70 <lteff) & (lteff<3.90)]) + \
			(-0.150651486316025*10.0**5*lteff[(3.70 <lteff) & (lteff<3.90)]**2.0) + (0.261724637119416*10.0**4*lteff[(3.70 <lteff) & (lteff<3.90)]**3.0) + \
			(-0.170623810323864*10.0**3*lteff[(3.70 <lteff) & (lteff<3.90)]**4.0)

	BCv[lteff> 3.90] = (-0.118115450538963*10.0**6) + (0.137145973583929*10.0**6*lteff[lteff> 3.90]) + \
			(-0.636233812100225*10.0**5*lteff[lteff> 3.90]**2.0) + (0.147412923562646*10.0**5*lteff[lteff> 3.90]**3.0) + \
			(-0.170587278406872*10.0**4*lteff[lteff> 3.90]**4.0) + (0.788731721804990*10.0**2*lteff[lteff> 3.90]**5.0)
	return BCv#,eBCv

def lum(V,eV ,para,epara, Av,eAv, BC,Mbolsol=4.73,eMbolsol=0.004,eBC=0.03):

	logl=4+(0.4*Mbolsol)-(2*np.log10(para))-0.4*(V-Av+BC)
	Lum=10**logl

	dlogl2=(0.4*eMbolsol)**2 + (2*(epara/para)* (1/np.log(10)))**2 + (0.4*eV)**2 +(0.4*eAv)**2 + (0.4*eBC)**2
	dlogl=np.sqrt(dlogl2)
	dLum=Lum*np.log(10)*dlogl

	return Lum,dLum,logl,dlogl

#lat =b long= l
def Av_bayes(l,b,para):
	d=1/(1e-3*para)#pc
	#print(d)
	d=d.values
	l=l.values
	b=b.values
	coords = SkyCoord(l*units.deg, b*units.deg,distance=d *units.pc, frame='galactic')
	bayestar = BayestarWebQuery(version='bayestar2017')
	eebv = bayestar(coords, mode='samples')
	eebv=np.std(eebv,axis=1)
	ebv = bayestar(coords, mode='median')
	ebv=2.742*ebv
	return ebv,eebv


stars=pd.read_csv('Final_Vals_all.txt',delimiter='\t',comment='#')
#+0.3 if gaia
stars=stars[['KIC', 'HIP', 'HD', 'Teff', 'eTeff', 'V', 'eV', 'GLON', 'GLAT', 'Para','ePara', 'Flag']]
stars['BC']=bolcorr(stars['Teff'],stars['eTeff'])

stars['AV_bayes'],stars['eAV_bayes']=Av_bayes(stars['GLON'],stars['GLAT'],stars['Para'])
print(stars['AV_bayes'])

stars['Lum_bay'],stars['eLum_bay'],stars['log10L_bay'],stars['elog10L_bay']=\
lum(stars['V'],stars['eV'],stars['Para'],stars['ePara'],stars['AV_bayes'],stars['eAV_bayes'],stars['BC'])

print(stars['Lum_bay'])
