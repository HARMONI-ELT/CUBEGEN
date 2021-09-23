# Input data cube generator

Written by Simon Zieleniewski & Nicholas Zieleniewski

Last Edited: 23-09-21



## PURPOSE:

This package produces simple input data cubes for simulations using the HSIM and NIFSIM pipelines for the ELT/HARMONI IFU. It can produce simple point or extended sources with template spectra or simple emission line profiles. The output FITS files are formatted to run through the pipelines.



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

1. cubename: Output data cube file name
2. userspec: Path to input spectrum datafile (wavelength[A], flux[erg/s/cm2/A]) - enter None if not using
3. userres: Resolution element of user spectrum [A] - enter 0 if not using
4. start_lambda: Start wavelength value [A] - enter anything if uploading spectrum
5. end_lambda: End wavelength value [A] - enter anything if uploading spectrum
6. R: Spectral resolving power - enter anything if uploading spectrum
7. ABmag: AB magnitude - enter anything if uploading spectrum
8. band: AB magnitude normalisation band [V, R, I, J, H, K, L, M] - enter anything if uploading spectrum
9. z: Redshift - enter anything if uploading spectrum'
10. spectype: Spectrum type [Flat, Emission, O5V, O9V, B0V, B3V, B9V, A0V, A3V, A5V, F0V, F2V, F5V, G0V, G2V, G5V, K0V, K2V, K5V, K7V, M0V, M2V, M3V, M4V, M5V, M6V, lyaem1, lyaem2, lyaem3, lyaem4]
11. spaxel_scale: Spaxel box size [mas]
12. fov: Field of view: [spaxels]
13. source_type: Source type [Point, Galaxy(=Sersic)]
14. num_sources: No. of sources [1,2]
15. source_sep: Separation of sources (if two) [spaxels] - enter value regardless!
16. sersic_k: Sersic k parameter - enter value regardless!
17. sersic_n: Sersic n parameter - enter value regardless!
18. brightness_ratio: Brightness ratio between two sources - enter value regardless!
19. linewave: Emission line central wavelength [A] - enter value regardless!
20. linewidth: Emission line width [km/s] - enter value regardless!
21. lineflux: Emission line total flux [erg/s/cm2] - enter value regardless!

Use -h or --help to display help message and exit
Use -c or --cline option to use command line.
Use -o or --odir when using command line to specify output file directory. Default is /hsim/Output_cubes/

An example command line entry:
$ python cubegen.py -c -o New_datacube None 0 5000 7000 4000 20 V 0 Flat 1 500 Galaxy 2 100 1 4 1.5 0 0 0

