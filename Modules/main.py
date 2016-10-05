'''Main code for generating input data cubes for HSIM
pipeline.

Author: Simon Zieleniewski & Nicholas Zieleniewski

Last updated: 05-10-16

'''


import numpy as np
import astropy.io.fits as pf
import time as time
import wx
#Import custom modules
import header_format as hf
import datacube_init as dc
import spaxelfunc as sf
import intensityprofiles as ip
import spectra as sp
import plotdata as pd
import mag_rescale as mr
import spec2cube as s2c


def main(headerdata, modeldata, userspec=None, userres=None):
    '''Define the parameters needed in the header of the FITS file, as well
       as gathering the spectrum data.
       
       Inputs:
    
            - headerdata  - List, sent from wxPython GUI.
            - modeldata   - List, sent from wxPython GUI.
            - userspec: data file with (lambda[A], flux[erg/s/cm2/A]) format
            - userres: Resolution of user supplied spectrum file [A]

       Outputs:

            - Data cube FITS file
       
       '''

    #---  HSIM header values  ---#
    CDELT1, CDELT2, CRVAL3, MAXWAVE, R, FUNITS, CRPIX3, CUNIT1,\
    CUNIT2, CUNIT3, CTYPE1, CTYPE2, CTYPE3, HRFAC = headerdata

    #---  HSIM cube parameters  ---#
    numgal, xspaxels, yspaxels, otype, z, mag, band, pixsep, fac, spec_type, \
    gauss_wave, gauss_width, gauss_flux, centre, grid, name, k, n = modeldata

    if userspec!=None and userres==None:
        print 'Must supply value for spectral resolution [A] when supplying input spectrum file'
        sys.exit()
    elif userres!=None and userspec==None:
        print 'Must supply spectrum data file (wavelength[A], flux[erg/a/cm2/A]) if supplying resolution value [A]'
        sys.exit()
    elif userspec!=None and userres!=None:
        spectrum, Lambda_0, CRVAL3, delta_lambda = s2c.userSpec(userspec)
        SPECRES = userres
        R = Lambda_0/float(SPECRES)
    else:
        print 'No user spectrum supplied'

        #----  Create spectra  -----#
        Lambda_0 = (CRVAL3+MAXWAVE)/2.
        delta_lambda=Lambda_0/(2.*R)
        SPECRES = delta_lambda*2.
        wavelengths=np.arange(CRVAL3,MAXWAVE+(delta_lambda/2.),delta_lambda)  #Wavelength values [Angstroms]
        spectrum=sp.initalise_spec(spec_type, wavelengths, z, gauss_wave, gauss_width, gauss_flux)   #Get spectrum

        #---  Scale the cube to the correct units  ---#
        if spec_type!='Emission':
            mr.rescale(datacube, mag, band, Lambda_0, 'one')      

    #---  Create data cube  ---#
    spaxels = [xspaxels, yspaxels]
    datacube=dc.datacube(spaxels, spectrum)

    #---  Apply relevant intensity profile and scale flux  ---#
    spans = [CDELT1*xspaxels, CDELT2*yspaxels]
    spaxdists = sf.r_values(spaxels, spans, centre)
    ip.initialise(numgal, otype, datacube, spaxdists, pixsep, fac, grid, k, n)

    #---  Scale to units of Flux/arcsec^2  ---#
    datacube /= (CDELT1*CDELT2)

    #Simulator only needs 32bit
    datacube=datacube.astype(np.float32)

    #---  Get HSIM/NIFSIM friendly hdu(list)  ---#
    values=[datacube.shape[2], datacube.shape[1], datacube.shape[0],
            CDELT1*1000., CDELT2*1000., delta_lambda, CRVAL3, FUNITS, CRPIX3, CUNIT1,
            CUNIT2, CUNIT3, CTYPE1, CTYPE2, CTYPE3, SPECRES]
    optionalkey_vals=[('Gridsize',grid),('Numgal',numgal),('xSpaxel',spaxels[0]),('ySpaxel',spaxels[1]),('Maxwave',MAXWAVE),\
                      ('Rpower', R), ('Redshift',z), ('ABMag', mag), ('2GalSep', pixsep),
                      ('2GalBOS', fac), ('spectype', spec_type), ('GFLUX', gauss_flux), ('GFWHM', gauss_width),\
                      ('Centre', centre), ('LAMBDA0', Lambda_0),\
                      ('name', name), ('KSersic', k), \
                      ('NSersic', n)]
    hdulist = hf.make_hdulist(datacube, values, optionalkey_vals)
    #Save the file
    hdulist.writeto('Generated_Cubes/'+name+'.fits', clobber=True, output_verify='ignore')

    #---  Print FITS info and plot data  ---#
    print hdulist.info()
    print hdulist[0].header
    print ''
    print 'Cube generation complete!'
    print ''