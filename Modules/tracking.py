# t.py

import numpy as np

from astropy.io import fits

hdulist = fits.open('/PATH TO /new_image.fits')      #path to new FITS file, edit!!
scidata = hdulist[0].data

#initalize array to keep track of what pixels are valid to be checked for cluster
#2 pixels wider than array in both dimensions for boundry conditions of get_nbr function
pixels_checked=np.zeros((len(scidata)+2, len(scidata[0])+2))
for x in range(len(scidata[0])+2):
    pixels_checked[0][x]=1
    pixels_checked[len(pixels_checked)-1][x]=1
for y in range(len(scidata)+2):
    pixels_checked[y][0]=1
    pixels_checked[y][len(pixels_checked[0])-1]=1
for x in range(len(scidata[0])):
    for y in range(len(scidata)):
        if scidata[y,x] == 0:
            pixels_checked[y+1][x+1]=1

#append to array and change pixels_checked value            
def ap (tpl, x, y):
    tpl.append([y,x])
    pixels_checked[y+1][x+1]=1

#check if pixel has already been checked
def if_checked(x,y):
    if pixels_checked[y+1][x+1]==1:
        return("yes")
    else:
        return("no")

#rest of this is for recursive clustering 
    
def get_track(trackmap, x,y):
    get_nbr(trackmap, x,y+1)
    get_nbr(trackmap, x-1,y+1)
    get_nbr(trackmap, x-1,y)
    get_nbr(trackmap, x-1,y-1)
    get_nbr(trackmap, x,y-1)
    get_nbr(trackmap, x+1,y+1)
    get_nbr(trackmap, x+1,y)
    get_nbr(trackmap, x+1,y+1)
    return

def get_nbr(trackmap, x,y):
    if y<len(scidata) and x<len(scidata[0]):
        if scidata[y,x]==1 and  if_checked(x,y)=="no":   #would use pixel_checked array to check validity, but this always gives stack error
            ap(trackmap, x,y)
            get_track(trackmap, x,y)
        return
        


