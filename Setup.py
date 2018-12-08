#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 03:05:15 2018

@author: emily
"""

import sys
#add path to where files tracking and Setup (in Modules folder) are kept, edit 
sys.path.append("/PATH TO /Modules")                        
sys.setrecursionlimit(20000)

from astropy.io import fits
import simplefitsfile as ssf 
import numpy as np

hdulist = fits.open('/PATH TO /Image37450.fits')  #path to original FITS file 
scidata = hdulist[0].data


#This section ONLY necassary for SNOLAB RAW images (to cut out left half of FITS file, which is base readout noise)
#half=int(len(scidata[0])/2)
#cut=np.zeros((len(scidata), half))
#for y in range(len(cut)):
#    for x in range(len(cut[0])):
#        cut[y][x]=int(scidata[y,x+half])
#scidata=cut

#get data without high outliers
values=[]
for n in range(len(scidata)):
    for k in range(len(scidata[0])):
        values.append(scidata[n,k])
scidataA=np.sort(values)
final=int(len(scidataA)*.996)

avg=ssf.avgvalue(scidataA, final)
sigma=ssf.sigma(scidataA, final, avg)
scidata=ssf.new_fits(scidata, avg, sigma)

hdulist.writeto('/PATH TO /new_image.fits')          #path to new FITS file 
