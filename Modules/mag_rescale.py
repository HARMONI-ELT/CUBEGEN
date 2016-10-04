'''Module to linearly rescale the flux in the datacube in order to
correctly model the desired AB magnitude, at the reference wavelength.

Author: Nicholas Zieleniewski, Simon Zieleniewski

Last updated: 15-04-16

'''


import numpy as np
import scipy.constants as sc
import SimpleNumericalCalculus as SNC


#------------#
def rescale(datacube, mag, band):
    '''Scales the flux correctly to match the provided magnitude.

    =========================== Input ==============================
    datacube       - 3D numpy array, storing a spectrum (dimesion 0)
                     for each spatial element.
    mag            - Float, AB magnitude, unitless. Desiried magnitude
                     of galaxy at ref_wavelength.
    band           - Photometric band for zeropoint
    ============================ Out ===============================
    datacube       - Datacube modified in place.'''

    bands = ['V', 'R', 'I', 'J', 'H', 'K', 'L', 'M']
    B_zp = 5.623413251903491e-09
    V_zp = 3.6307805477010106e-09
    R_zp = 2.6302679918953816e-09
    I_zp = 1.6982436524617462e-09
    J_zp = 7.244359600749892e-10
    H_zp = 4.0738027780411227e-10
    K_zp = 2.29086765276777e-10
    L_zp = 9.120108393559117e-11
    M_zp = 4.7863009232263794e-11
    ZPs = [B_zp, V_zp, R_zp, I_zp, J_zp, H_zp, K_zp, L_zp, M_zp]

    flux_zeropoint = ZPs[bands.index(band)]

    datacube *= (flux_zeropoint)
#------------#


#------------#
def rescale_gauss(datacube, lambda_0, gauss_flux, delta_lambda):
    '''Scales the flux correctly to match the provided magnitude.

    =========================== Input ==============================
    datacube       - 3D numpy array, storing a spectrum (dimesion 0)
                     for each spatial element.
    Lamda_0        - Wavelength for conversion between /Hz -> /A
    gauss_flux     - Total integrated flux that should be under the
                     gaussian curve.
    delta_lambda   - Wavelength step for integration.
    ============================ Out ===============================
    datacube       - Datacube modified in place.'''

    spectra=np.sum(np.sum(datacube,axis=1),axis=1)
    integrated_flux=SNC.int_simp(spectra, delta_lambda)
    datacube*=gauss_flux/integrated_flux
#------------#