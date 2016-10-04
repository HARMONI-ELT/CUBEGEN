'''Module to plot some data for the EAGLE sim project

by Nicholas Zieleniewski of Durham University.'''


#Import
import numpy as np
import pylab
from matplotlib import cm  #Colour maps

#Import custom modules
from spaxelfunc import r_values
import intensityprofiles as ip
#from DurhamModules.Maths import SimpleNumericalCalculus as SNC

def plotdata(datacube, wavelengths, spectrum, span, spaxels, k, n, centre):
    '''Plots data collected by main.py'''

    #make some r values and get I(r):
    r=np.linspace(0., span, 200)
    sersic=np.exp(-k*(r/0.15)**(1./n))
    
    #Display datacube, spectrum and I(r):
    sum_=np.sum(datacube, axis=0)
    pylab.subplot('311')
    pylab.imshow(sum_, interpolation='nearest', cmap=cm.hot)
    pylab.subplot('312')
    pylab.plot(r,sersic, color='black')
    pylab.yscale('log')
    pylab.xlabel('Radius, r / [arcsec]')
    pylab.ylabel('Intensity (normalised)')
    pylab.axis([0.,.8, 0.001,1])
    pylab.subplot('313')
    pylab.plot(wavelengths, spectrum)
    pylab.show()

    #Display image again in larger window
    spectra=np.sum(np.sum(datacube, axis=1),axis=1)
    print np.mean(spectra)
    sum_[3:15,3]=np.max(sum_)
    pylab.imshow(sum_, interpolation='nearest', cmap=cm.gist_heat, extent=[-0.7875,0.7875,-0.7875,0.7875])
    pylab.savefig('image.pdf')
    pylab.show()
    spec=np.sum(np.sum(datacube[:,0:spaxels, 0:spaxels], axis=1),axis=1)
    pylab.plot(wavelengths, spec)
    pylab.plot(wavelengths, np.sum(np.sum(datacube[:,0:spaxels, 0:spaxels]*np.less(r_values(spaxels, span, centre), 0.15), axis=1),axis=1))
    pylab.axis([10500,13500,0,np.max(spec)*1.1])
    pylab.xlabel('Wavelength, Angstroms')
    pylab.ylabel('Flux, ergs/s/cm2/A')
    pylab.savefig('totalflux.pdf')
