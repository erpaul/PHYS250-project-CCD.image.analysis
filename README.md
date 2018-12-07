# PHYS250-project-CCD.image.analysis

This program will find the intersection points of particle track paths in CCD images in FITS file format, and produce a heatmap of those points.  

After downloading the files, it is important to run Setup first, which will add the Modules folder to your path and convert the pixel values of the CCD image to 0 or 1, and save it as a new image. Then, edit the tracking file in the Modules folder to read data from the new image (instructions in file). Finally, edit the track_intersections file to also read data from the new image and save the heatmap produced to your desired location. 

SAOImageDS9 is a good way to view the FITS files, but that is not necessary for the program to run.
