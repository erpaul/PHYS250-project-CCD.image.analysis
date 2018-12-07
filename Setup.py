#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 03:05:15 2018

@author: emily
"""

import sys
#add path to where files tracking and Setup (in Modules folder) are kept, edit 
sys.path.append("/PATH TO /Modules")                        
sys.setrecursionlimit(10000)



from astropy.io import fits
import simplefitsfile as ssf 

hdulist = fits.open('/PATH TO /Image37450.fits')  #path to original FITS file 
scidata = hdulist[0].data

avg=ssf.avgvalue(scidata)
sigma=ssf.sigma(scidata, avg)
scidata=ssf.new_fits(scidata, avg, sigma)

hdulist.writeto('/PATH TO /new_image.fits')          #path to new FITS file 
