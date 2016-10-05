'''

Module to initialise a test datacube for running through the HSIM/NIFSIM
simulators

Authors: Nicholas Zieleniewski & Simon Zieleniewski

Last updated: 05-10-16
   
'''

#import
import numpy as np

#------------#
def datacube(spaxels, spectrum):
    '''Initialses a datacube (3D numpy array) containing a mock lyman
       alpha break spectra for each spaxel. Each spectra has a spectral
       resolution of R. 

       =========================== Input ==============================
       spaxels       - List, number of spaxels in [y, x] directions.
                       x-y grid in the format: datacube[Intensity, y, x].
       spectrum      - 1D numpy array, contains float values corresponding
                       to the intensity at a cetain (known) wavelength.

       ============================ Out ===============================
                    --- Datacube is modified inplace ----           '''
     
    a=spectrum.shape[0]
    spectrum.shape=a,1,1                   #Reshape to fill datacube
    datacube=np.empty([a,spaxels[1],spaxels[0]]) #make empty array of correct size
    datacube[:,:,:]=spectrum               #Fill all points on spaxel grid with the spectrum
    spectrum.shape=a                       #Return to old shape
    return datacube
#------------#

#------------#
def Tesselate(datacube, spaxels, grid):
    '''Initialses a datacube (3D numpy array) containing a mock lyman
       alpha break spectra for each spaxel. Each spectra has a spectral
       resolution of R. 

       =========================== Input ==============================
       datacube      - Single datacube to be copied grid*grid times.
       spectrum      - 1D numpy array, contains float values corresponding
                       to the intensity at a cetain (known) wavelength.
       grid          - int, gives the number of images that should be
                       present in each datacube as grid x grid.

       ============================ Out ===============================
       newcube       - Tesselated datacube.'''
    

    #Make new empty datacube
    d0=datacube.shape[0]
    d1=datacube.shape[1]
    d2=datacube.shape[2]
    newcube=np.empty([d0, d1*grid, d2*grid])

    #Loop over new cube and copy cube
    for i in xrange(0, grid, 1):
        starti=spaxels*i
        endi=spaxels*(i+1)
        for j in xrange(0, grid, 1):
            startj=spaxels*j
            endj=spaxels*(j+1)
            newcube[:,starti:endi,startj:endj]=datacube.copy()
            if i==2 and j==2:
                newcube[:,starti:endi,startj:endj]=0
            if i==0 and j==2:
                newcube[:,starti:endi,startj:endj]=0
            if i==3 and j==1:
                newcube[:,starti:endi,startj:endj]=0
                
    #Return tesselated datacube
    return newcube
#------------#

#------------#
def path_setup(path):
    '''function to setup paths to datafiles'''
    import os
    script_dir = os.path.split(os.path.abspath(__file__))[0]
    out_path = os.path.join(script_dir, os.path.relpath(path),'')

    return out_path
#------------#
    
