'''

Module that contains the correct header format for datacubes
submitted to the E-ELT/HARMONI Simulator. Also contains a function
that updates the Pyfits produced header to contains the relevant
keywords and values.

Author: Nicholas Zieleniewski and Simon Zieleniewski

Last updated: 06-10-16

'''


#Import:
import astropy.io.fits as pf


def keywords():
    '''Just a function to contain the keys needed for the HARMONI simulator'''
    
    keywords=['NAXIS1', 'NAXIS2', 'NAXIS3', 'CDELT1', 'CDELT2',\
              'CDELT3', 'CRVAL3', 'BUNIT', 'CRPIX3', 'CUNIT1',\
              'CUNIT2', 'CUNIT3', 'CTYPE1', 'CTYPE2', 'CTYPE3',\
              'SPECRES']
    return keywords


def make_hdulist(datacube, values, opt_key_vals):
    '''Updates the Pyfits produced header to include the keys and their
       values and needed by the HARMONI simulator.

       =========================== Input ==============================
       datacube      - 3D numpy array. Contains spectral data over the
                       x-y grid in the format: datacube[Intensity, y, x].
       values        - List. Contains values for the keys in keywords().
       opt_key_vals  - List. Contains optional key words and values in
                       the format [(key1, val1), (key2, val2), etc... ]

       ============================ Out ===============================
       hdulist       - Pyfits created hdulist (containing only a primary
                       hdu). Properly formatted with the given keywords
                       and values for the header.''' 
    
    hdu=pf.PrimaryHDU(datacube)              #Primary HDU object to hold our datacube
    hdulist=pf.HDUList([hdu])                #Create a list to hold the new HDU
    primhdr=hdulist[0].header                #Get primary header keywords and values/comments

    sim_hdr=keywords()                  #List of neccessary keywords as given in the EAGLE sim documentation
    sim_hdr=zip(sim_hdr,values)    #list of keywords and values as [[key,val],[key,val]....]
        
    for key_val in sim_hdr:             #Update the pimary data cube header with the key words and values
        primhdr.set(key_val[0], key_val[1])

    for key_val in opt_key_vals:             #Update the pimary data cube header with optional key words and values
        primhdr.set(key_val[0], key_val[1])  

    return hdulist                           #Return hdulist
