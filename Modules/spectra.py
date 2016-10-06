'''

Module containing functions that return various different
template spectra for use in the HSIM/NIFSIM simulators

Author: Nicholas Zieleniewski, Simon Zieleniewski


Last updated: 06-10-16

'''

#import
import numpy as np
import astropy.io.fits as p
from scipy.interpolate import interp1d

def initalise_spec(spec_type, wavelengths, z, linewave, linewidth, lineflux):
    '''Given the string spec_type, the correct spectrum is returned'''

    #Pickles spectra
    stars = ['O5V','O9V','B0V','B3V','B9V','A0V','A3V',
         'A5V','F0V','F2V','F5V','G0V','G2V','G5V','K0V','K2V',
         'K5V','K7V','M0V','M2V','M3V','M4V','M5V','M6V']

    #Lyman Break galaxy spectra given by M. Swinbank - 19-11-15
    lbgs = ['lyaem1', 'lyaem2', 'lyaem3', 'lyaem4']

    if spec_type in stars:
        spectrum = np.loadtxt('./Simul_spectra/pickles_spectra/'+spec_type+'.dat')
        #Apply redshift correction
        if z != 0.:
            print 'redshift = %.1f' % z
            new_waves = z_correct(spectrum[:,0], spectrum[:,1], z)
            interp_spec = interp1d(new_waves ,spectrum[:,1], kind='linear')
        elif z == 0.:
            print 'No redshift!'
            interp_spec = interp1d(spectrum[:,0] ,spectrum[:,1], kind='linear')

        new_spec = interp_spec(wavelengths)

    elif spec_type in lbgs:
        spectrum, head = p.getdata('./Simul_spectra/lyman_alpha_spectra/'+spec_type+'.fits', header=True)
        spectrum /= np.median(spectrum)
        lams = np.linspace(head['CRVAL1'], head['CRVAL1'] + (head['NAXIS1']-1)*head['CDELT1'], head['NAXIS1'])
        #Apply redshift correction
        if z != 0.:
            print 'redshift = %.1f' % z
            new_waves = z_correct(lams, spectrum, z)
            interp_spec = interp1d(new_waves ,spectrum, kind='linear')
        elif z == 0.:
            print 'No redshift!'
            interp_spec = interp1d(lams ,spectrum, kind='linear')

        new_spec = interp_spec(wavelengths)

    elif spec_type=='Emission':
        new_spec = Gauss(wavelengths, z, linewave, linewidth, lineflux)

    elif spec_type=='Flat':
        new_spec = np.ones(len(wavelengths), dtype=np.float64)

    return new_spec
#------------#


#------------#
def z_correct(wavelengths, spectrum, z):
    loglambs = np.linspace(np.log10(wavelengths[0]),np.log10(wavelengths[-1]),len(wavelengths))
    loglambs = loglambs + np.log10(1 + z)
    lambs = np.round(10**loglambs, decimals=1)
    new_waves = np.linspace(lambs[0], lambs[-1], len(lambs))
    return new_waves
#------------#


#------------#
def Gauss(wavelengths, z, line_wave, gauss_width, line_flux):
   '''Creates a mock lyman-break spectrum using a fermi-dirac type function.
   The lyman beak is very clear, going from '0' to '1' in a step.

   =========================== Input ==============================
   wavelengths   - 1D numpy array, Contains values of wavelengths in
                   Angstroms.
   z             - Float, redshift used to position Lyman-break
   line_wave     - Float, wavelength of line [A]
   gauss_width   - Float, Full Width Half Maximum of Guassin, given
                   in km/s.
   line_flux     - Float, Flux of line [erg/s/cm2]
   ============================ Out ===============================
   spectrum      - 1D numpy array. Contains the corresponding flux
                   for each wavelength value (normalised).'''

   #make the spectrum:
   nline_wave=line_wave*(z+1)
   gauss_width*=nline_wave/3.E5  #Convert km/s to Angstroms equivalent (FWHM)
   sigma=gauss_width/(2*np.sqrt(2*np.log(2)))
   spectrum=np.exp(-((wavelengths-nline_wave)**2)/(2*sigma**2))
   spectrum[np.where(wavelengths>nline_wave+5*sigma)]=0.
   spectrum[np.where(wavelengths<nline_wave-5*sigma)]=0.
   spectrum /= line_flux
   return spectrum
#------------#