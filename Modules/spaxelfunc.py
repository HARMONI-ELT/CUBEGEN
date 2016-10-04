'''Module containing a function that creates a 2D array with elements storing
the distance they are from the 'centre' of the array.

by Nicholas Zieleniewski of Durham University.'''

import numpy as np

def r_values(spaxels, spans, centre):
    '''Generates an array of size [spaxels,spaxels] containing the distance
       of each element from the centre point of the array.

       =========================== Input ==============================
       spaxels       - List, number of spaxels in [y, x] directions.
                       x-y grid in the format: datacube[Intensity, y, x].
                       (Should be even)
       span          - List, the width of the edges of the image in arc
                       seconds.
       centre        - BOOL, if True, image is central, if False then
                       image is offset to centre on a pixel at just off
                       the centre of the spaxel array.
       ============================ Out ===============================
       r             - 2D numpy array. Contains the distance of each
                       element from the centre point of the array.'''

    if centre:
        incrx=spans[0]/(2*spaxels[0])#Half a spaxel width in arcsec
        incry=spans[1]/(2*spaxels[1])#Half a spaxel width in arcsec
        x=np.linspace(-(spans[0]/2.)+incrx,(spans[0]/2.)-incrx,spaxels[0])
        y=np.linspace(-(spans[1]/2.)+incry,(spans[1]/2.)-incry,spaxels[1])
        
    elif not centre:
        i=(spaxels[0]/2)-1
        j=(spaxels[1]/2)-1
        incrx=spans[0]/(2*spaxels[0])#Half a spaxel width in arcsec
        incry=spans[1]/(2*spaxels[1])#Half a spaxel width in arcsec
        x=np.linspace(-i*2*incrx,(spans[0]/2.),spaxels[0])
        y=np.linspace(-j*2*incry,(spans[1]/2.),spaxels[1])

    cart=np.meshgrid(x,y)
    r=np.sqrt(cart[0]**2+cart[1]**2)        #Pythagoras
    return r
    

##def circleshape(datacube, r, lim):
##    '''Takes the input data cube and set all array outside the radial
##       lim values [arsec] to 0. 
##
##       =========================== Input ==============================
##       datacube      - 3D numpy array. Contains spectral data over the
##                       x-y grid in the format: datacube[Intensity, y, x].
##       r             - 2D numpy array. Contains the distance of each
##                       element from the centre point of the array.
##       lim           - Float, 'radius' of circle representing galaxy
##                       image.
##       ============================ Out ===============================
##                    --- Datacube is modified inplace ----           '''
##
##    #perform calculation:
##    datacube*=np.less(r, lim)

