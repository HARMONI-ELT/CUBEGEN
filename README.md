# Input data cube generator

Written by Simon Zieleniewski & Nicholas Zieleniewski

Last Edited: 03-10-16



## PURPOSE:

This package produces simple input data cubes for simulations using the HSIM and NIFSIM pipelines for the E-ELT/HARMONI and JWST/NIRSpec IFUs respectively. It can produce simple point or extended sources with template spectra or simple emission line profiles. The output FITS files are formatted to run through the pipelines.



## FILES:

The pipeline currently runs using the main python file:
```
cubegen.py

which requires several routines in the Modules/ subdirectory:

main.py

spectra.py
spaxelfunc.py
plotdata.py
mag_rescale.py
intensityprofiles.py
header_format.py
datacube_init.py
SimpleNumericalCalculus.py
```

There are also several data files:

Simul_spectra/pickles_spectra/ - contains stellar spectra for use as input templates
Simul_spectra/lyman_alpha_spectra/ - contains Lyman-alpha emission line template spectra



## DEPENDENCIES:

The following Python modules are essential to run the pipeline:
numpy - http://www.scipy.org/scipylib/download.html
scipy - http://www.scipy.org/scipylib/download.html
astropy - http://www.astropy.org/

The following is strongly recommended for optimum running:
wxPython - This is used to load the GUI. It can be downloaded from: http://www.wxpython.org/download.php


Make sure the modules can by found by your Python implementation. E.g. in a Python environment try:
```python
        >>> import numpy
        >>> import astropy
        >>> import scipy
        >>> import wx
```

there should be no errors!



## HOW TO USE:

The code can be run in two ways:

1. Running the GUI:
``$ python cubegen.py``
This opens the graphical interface from which you can enter the various parameters and start the simulation.

2. From the command line:
``$ python cubegen.py -c arg1 arg2 arg3 etc…``

Use:
``$ python cubegen.py -c``
to display arguments list
	
The commands must be entered in the following order:

1. datacube: Input datacube filepath
2. DIT: Exposure time [s]
3. NDIT: No. of exposures
4. band: Photometric band [V+R, Iz+J, H+K, V, R, Iz, J, H, K, V-high, R-high, z, J-high, H-high, K-high, None]
5. x-spax: x spatial pixel (spaxel) scale [mas]
6. y-spax: y spatial pixel (spaxel) scale [mas]
7. telescope: Telescope type (E-ELT, VLT)
8. AO: AO mode (LTAO, SCAO, Gaussian)
9. seeing: Atmospheric seeing FWHM [arcsec] - Between 0.67"-1.10"
10. zenith_ang: Zenith angle [deg]
11. user_PSF: Path to user uploaded PSF file - Enter None if not required
12. PSF blur: Additional telescope jitter [mas]
13. Site_temp: Site/telescope temperature [K]
14. Spec_Nyquist: (True/False) - Set spectral sampling to Nyquist sample spectral resolution element
15. Spec_samp: Spectral sampling [A/pix] - Only used if Spec_Nyquist = False, but enter a value regardless!
16. Noise_force_seed: Force random number seed to take a set value (0=No, 1-2=yes and takes that value)
17. Remove_background: (True/False) - Subtract background spectrum
18. Return_object: (True/False) - Return object cube
19. Return_transmission: (True/False) - Return transmission cube
20. Turn ADR off: (True/False)

Use -h or --help to display help message and exit
Use -c or --cline option to use command line.
Use -o or --odir when using command line to specify output file directory. Default is /hsim/Output_cubes/
Use -p or --proc when using command line to specify number of cores for parallel processing. Default is N_PROC-1 (if N_PROC>1)

An example command line entry:
$ python cubegen.py -c -p 5 -o /Path/to/output_dir/ /Path/to/Input_cubes/Input_cube.fits 900 20 H+K 20. 20. E-ELT LTAO 0.67 0. None 0. 280.5 True 1. 0 True True True

