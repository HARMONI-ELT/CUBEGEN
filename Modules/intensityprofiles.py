'''Module containing intensity profile functions that may be applied
to given data cubes in order to simulate varying surface brightness
of imaged galaxies.

by Nicholas Zieleniewski of Durham University.'''

import numpy as np

def initialise(numgal, otype, datacube, spaxdists, sep, fac, grid, k, n):
    '''Given the int numgal, the correct intensity profile
       is applied to the datacube inplace'''
    if numgal==1:
        print 'DATACUBE SHAPE', datacube.shape
        datacube*=I_profile(spaxdists, otype, k, n)
    elif numgal==2:
        datacube*=double_gal(spaxdists, otype, sep, fac, grid, k, n)
    elif numgal!=1 and numgal!=2:
        print 'ERROR - unsupported number of objects'


def I_profile(r, otype, k, n):
    '''Takes the radius values in the array and returns the intensity profile.
    A radial intensity distribution (power law) created from inspection of
    results in Oesch 2009 is implemented.

    =========================== Input ==============================
    r             - ND numpy array. Contains the distance of each
                    element from the centre point of the array.
    grid          - Int, number of tesselated cubes along one side.
    k             - Float, Sersic parameter.
    n             - Float, Sersic parameter.
    ============================ Out ===============================
    I             - ND numpy array. Contains the intensity profile that
                    results from using r values.'''
    if otype=='Point':
        x = np.where(r==r.min())
        print x
        r = np.where(r==r.min(), 1., 0.)
#        r[x[0]-1,x[1]-1] = 1.
#        r[x[0]-1,x[1]] = 1.
#        r[x[0],x[1]-1] = 1.
#        r *= 0.25
        print r[x[0]-2:x[0]+3,x[1]-2:x[1]+3]
        
        return r
    elif otype=='Galaxy':
        #Produce sersic intensity map
        sersic=np.exp(-k*(r/0.15)**(1./n))
        return sersic


def double_gal(r, otype, sep, fac, grid, k, n):
    '''Takes the radius values in the array and returns an intensity profile
    that mimics two galaxies seperated by 'sep' number of pixels. A radial
    intensity distribution (power law) created from inspection of results in
    Oesch 2009 is implemented. The function I_profile is called and centered
    at two different locations on the spaxel grid.

    =========================== Input ==============================
    r             - ND numpy array. Contains the distance of each
                    element from the centre point of the array.
    sep           - Float, seperation of the two intensity profile
                    centres in numbers of pixels.
    fac           - Float, a factor to modify the relative brightness
                    of the galaxies.
    grid          - Int, number of tesselated cubes along one side.
    k             - Float, Sersic parameter.
    n             - Float, Sersic parameter.
    ============================ Out ===============================
    I             - ND numpy array. Contains the intensity profile that
                    results from using r values.'''
    if otype=='Point':
        #spaxels (y, x)
        spaxels=r.shape

        #An empty array for the intensity profile
        I=np.empty([spaxels[0]*grid, spaxels[1]*grid])

        #perform calculations:
        i=r.shape[1]
        holder=np.zeros([spaxels[0],i+sep])
        Sersic=I_profile(r, otype, k, n)
        holder[:,0:i]=np.copy(Sersic)
        holder[:,sep::]+=fac*Sersic
        Sersic=holder[:,(sep/2):i+(sep/2)]
        Sersic/=np.max(Sersic)              #Normalise because of addition above 

        #Fill all points on spaxel grid with the I(r) profile 
        for i in xrange(0, grid, 1):
            starti=grid*i
            endi=spaxels[0]*(i+1)
            for j in xrange(0, grid, 1):
                startj=spaxels[1]*j
                endj=spaxels[1]*(j+1)
                I[starti:endi,startj:endj]=Sersic       
        return I
    
    elif otype=='Galaxy':
        #spaxels (y, x)
        spaxels=r.shape

        #An empty array for the intensity profile
        I=np.empty([spaxels[0]*grid, spaxels[1]*grid])

        #perform calculations:
        i=r.shape[1]
        holder=np.zeros([spaxels[0],i+sep])
        Sersic=I_profile(r, otype, k, n)
        holder[:,0:i]=np.copy(Sersic)
        holder[:,sep::]+=fac*Sersic
        Sersic=holder[:,(sep/2):i+(sep/2)]
        Sersic/=np.max(Sersic)              #Normalise because of addition above 

        #Fill all points on spaxel grid with the I(r) profile 
        for i in xrange(0, grid, 1):
            starti=grid*i
            endi=spaxels[0]*(i+1)
            for j in xrange(0, grid, 1):
                startj=spaxels[1]*j
                endj=spaxels[1]*(j+1)
                I[starti:endi,startj:endj]=Sersic       
        return I
    
    
