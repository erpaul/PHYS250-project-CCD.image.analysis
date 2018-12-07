#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 03:05:15 2018

@author: emily
"""

import sys
sys.path.append("/home/emily/Desktop/250project/Modules")                        #path to where files tracking and Setup are kept
sys.setrecursionlimit(10000)



from astropy.io import fits
import simplefitsfile as ssf 

hdulist = fits.open('/home/emily/Desktop/250project/FITSfiles/Image37450.fits')  #path to original fits file
scidata = hdulist[0].data

avg=ssf.avgvalue(scidata)
sigma=ssf.sigma(scidata, avg)
scidata=ssf.new_fits(scidata, avg, sigma)

hdulist.writeto('/home/emily/Desktop/250project/FITSfiles/image3.fits')          #path to new fits file 