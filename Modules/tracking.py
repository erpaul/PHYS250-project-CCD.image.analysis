# t.py

import numpy as np

from astropy.io import fits

hdulist = fits.open('/home/emily/Desktop/250project/FITSfiles/image7.fits')      #path to file
scidata = hdulist[0].data

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
# add an ordered pair to array
# pass in array and x,y point
def ap (tpl, x, y):
    tpl.append([y,x])
    pixels_checked[y+1][x+1]=1
    #np.sort(-tpl)
    #print (tpl)
   

def if_found(tpl, x,y):
    if [x,y] in tpl:
        return (0)
    else:
        return ("no") 

def if_checked(x,y):
    if pixels_checked[y+1][x+1]==1:
        return("yes")
    else:
        return("no")

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
    if pixels_checked[y+1][x+1]==0:
        ap(trackmap, x,y)
        get_track(trackmap, x,y)
    return
        


