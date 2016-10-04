'''

Function to generate spectrum from user supplied spectrum data file in format:
(wavelength[A], flux[erg/s/cm2/A])

Author: Sarah Kendrew & Simon Zieleniewski

Last updated: 04-10-16


'''


import numpy as np
import astropy.io.fits as fits
import astropy.io.ascii as ascii
import astropy.units as u
import os


def userSpec(fname, specres, outfile='harmoni_cube.fits'):
    
    '''This function will take a 1D spectrum and convert it to a cube that can be used as input for the HARMONI Simulator. 
    
    Input:
    - fname:    an ASCII filename containing the spectrum, formatted in 2 columns representing (wavelength[A], flux[erg/s/cm2/A])
    - specres:  the spectral resolution of the input spectrum, defined as the FWHM in Angstroms
    
    Optional input:
    - outfile:  the output filename
    
    The input file should contain 2 columns for wave and flux. We assume: 
    - wavelength in ANGSTROMS 
    - wavelength axis is uniformly sampled (ie. delta(wave) is constant)
    - flux in ERG/S/CM^2/ANGSTROMs. 
    
'''   
    # cols = ['wave', 'flux']
    # read in the spectrum from an ascii file. assume 2 columns: wave, flux. 
    # NOTE: 
    #  - if your filename has a header, update the data_start parameter to indicate where the table starts
    #  - you can set the delimiter manually using keyw
    # s = ascii.read(fname, names=cols, data_start=1)
    # nspec = len(s['wave'])
    # dwave = np.diff(s['wave'])[0]

    try:
        data = n.genfromtxt(fname)
    try:
        data = n.genfromtxt(fname, delimiter=',')
    except:
        print 'Cannot figure out delimiter!'
        print 'Use either single space of comma-separated values'
        print ''
        sys.exit()
    
    waves = data[:,0]
    flux = data[:,1]

    CRVAL3 = waves[0]
    Lambda_0 = (waves[0]+waves[-1])/2.
    delta_lambda = waves[1]-waves[0]

    return flux, Lambda_0, CRVAL3, delta_lambda
    