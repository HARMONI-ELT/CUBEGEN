'''

Code contianing GUI and command line options
for data cube generation interface for HSIM
(or general input datacubes)

Author: Simon Zieleniewski & Nicholas Zieleniewski

Last updated: 05-10-16

'''


import wx
from Modules import main
from Modules import spectra as sp


import getopt
import sys
import os
import numpy as n
from Modules import main
from Modules import spectra as sp
import commands
from Modules.datacube_init import path_setup



if __name__=="__main__":
  
    optlist, args = getopt.getopt(sys.argv[1:], 'hcp:o:', ['help', 'cline', 'proc', 'odir'])

    for o, a in optlist:
        if o in ("-h", "--help"):
            print""
            print '    --------     '
            print 'Data Cube Generator'
            print '    --------     '
            print"---"
            print 'TO RUN'
            print 'GUI'
            print '>>> python cubegen.py'
            print""
            print 'Command line'
            print '>>> python cubegen.py -c arg arg2 ...'
            print"---"
            print 'OPTIONS'
            print '-h or --help = display this message and exit'
            print '-c or --cline = use command line. Use: >>> python cubegen.py -c to display arguments list'
            #print '-p or --proc = set the number of processors when using command line (1-'+str(mp.cpu_count())+')'
            print '-o or --odir = set the output file directory when using the command line (default: /hsim-#/Output_cubes)'
            print""
            sys.exit()

#     nprocs = mp.cpu_count()-1           
#     for o, a in optlist:
#         if o in ("-p", "--proc"):
#             nprocs = int(a)
#             if nprocs > mp.cpu_count():
#                 print 'Only '+str(mp.cpu_count())+' CPUs. Using '+str(mp.cpu_count())
#                 nprocs = mp.cpu_count()
                
    odir = path_setup('../Generated_Cubes/')         
    for o, a in optlist:
        if o in ("-o", "--odit"):
            if os.path.exists(a) and os.path.isdir(a):
                odir = a
            elif not os.path.exists(a):
                print "OUTPUT DIRECTORY DOESN'T EXIST (OR IS NOT A DIRECTORY)! PLEASE CHOOSE AGAIN. EXITING"
                sys.exit()
            
    for o, a in optlist:
        if o in ("-c", "--cline") and len(args) != 20:
            print""
            print 'COMMAND LINE USAGE'
            print ""
            print 'Enter command line arguments in following order:'
            print '1. cubename: Output data cube file name'
            print '2. userspec: Path to input spectrum datafile (wavelength[A], flux[erg/s/cm2/A]) - enter None if not using'
            print '3. userres: Resolution element of user spectrum [A] - enter None if not using'
            print '4. start_lambda: Start wavelength value [A] - enter anything if uploading spectrum'
            print '5. end_lambda: End wavelength value [A] - enter anything if uploading spectrum'
            print '6. R: Spectral resolving power - enter anything if uploading spectrum'
            print '7. ABmag: AB magnitude - enter anything if uploading spectrum'
            print '8. band: AB magnitude band [V, R, I, J, H, K, L, M] - enter anything if uploading spectrum'
            print '9. z: Redshift - enter anything if uploading spectrum'
            print '10. spectype: Spectrum type [Flat, Emission, O5V, O9V, B0V, B3V, B9V, A0V, A3V, A5V, F0V, F2V, F5V, G0V, G2V, G5V, K0V, K2V, K5V, K7V, M0V, M2V, M3V, M4V, M5V, M6V, lyaem1, lyaem2, lyaem3, lyaem4]'
            print '11. spaxel_scale: Spaxel box size [mas]'
            print '12. fov: Field of view: [spaxels]'
            print '13. source_type: Source type [Point, Galaxy(=Sersic)]'
            print '14. num_sources: No. of sources [1,2]'
            print '15. source_sep: Separation of sources (if two) [spaxels]'
            print '16. sersic_k: Sersic k parameter'
            print '17. sersic_n: Sersic n parameter'
            print '18. brightness_ratio: Brightness ratio between two sources'
            print '19. linewave: Emission line central wavelength [A]'
            print '20. linewidth: Emission line width [km/s]'
            print '21. lineflux: Emission line total flux [erg/s/cm2]'
            print ""
            sys.exit()
        elif o in ("-c", "--cline") and len(args) == 20:
            print args
            name = str(srgs[0])
            userspec = str(args[1])
            userres = float(args[2])
            start_lambda = float(args[3])
            end_lambda = float(args[4])
            R = float(args[5])
            ABmag = float(args[6])
            band = str(args[7])
            z = float(args[8])
            spectype = str(args[9])
            spaxel_scale = float(args[10])
            fov = float(args[11])
            source_type = str(args[12])
            num_sources = int(args[13])
            source_sep = int(args[14])
            sersic_k = float(args[15])
            sersic_n = float(args[16])
            brightness_ratio = float(args[17])
            linewave = float(args[18])
            linewidth = float(args[19])
            lineflux = float(args[20])
            crpix3 = 1               #CRPIX1
            cunit1 = 'mas'           #CUNIT1
            cunit2 = 'mas'           #CUNIT2
            cunit3 = 'angstroms'     #CUNIT3
            ctype1 = 'RA'            #CTYPE1
            ctype2 = 'DEC'           #CTYPE2
            ctype3 = 'WAVELENGTH'    #CTYPE3
            specr = R                #RPOWER
            funits = 'erg/s/cm2/A/arcsec2/'
            centre = 1
            grid = 1

            #Collect parameters into lists
            headerdata = [spax, spax, start_lambda, end_lambda, R,
            crpix3, cunit1, cunit2, cunit3, ctype1, ctype2, ctype3]
            modeldata = [num_sources, fov, fov, source_type, z, ABmag, band,
            source_sep, brightness_offset, spectype, linewave, linewidth, lineflux, centre, grid,
            name, sersic_k, sersic_n]
            #Start main program
            main.main(headerdata, modeldata, userspec, userres, odir)
        

    #Use GUI interface if no command line option
    wxfound = 0
    if len(optlist) == 0 and len(args) == 0:
        try:
            import wx
            wxfound = 1
            class Form1(wx.Frame):
                
                def __init__(self, parent, title):
                    super(Form1, self).__init__(parent, title=title, 
                        size=(1100, 400))

                    self.InitUI()
                    self.Centre()
                    self.Show()

                def InitUI(self):

                    panel = wx.Panel(self)
                    titlefont = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
                    subtitlefont = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)

                    # Set up the menu.
                    filemenu  = wx.Menu()
                    menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
                    menuExit  = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

                    # Creating the menubar.
                    menuBar = wx.MenuBar()
                    menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
                    self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

                    # Events.
                    self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
                    self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
                    
                    hbox = wx.BoxSizer(wx.HORIZONTAL)

                    fg = wx.FlexGridSizer(11, 2, 15, 10)

                    #Spectral parameters
                    spect = wx.StaticText(panel, label='Spectral Parameters')
                    spect.SetFont(titlefont)        
                    subspect = wx.StaticText(panel, label=' ')
                    INPUTSPEC = wx.StaticText(panel, label="Input Spectrum")
                    self.INPUTSPECVAL = wx.FilePickerCtrl(panel, path="None")
                    USERRES = wx.StaticText(panel, label="Resolution [A]")
                    self.USERRESVAL = wx.TextCtrl(panel, value='0')
                    orlabel = wx.StaticText(panel, label='OR')
                    orlabel.SetFont(titlefont)        
                    suborlabel = wx.StaticText(panel, label=' ')

                    SPECTRA = wx.StaticText(panel, label="Spectrum Type:")
                    self.SPECTRAVAL = wx.Choice(panel, choices=['Flat','Emission','Absorption','O5V',
                                                        'O9V','B0V','B3V','B9V','A0V','A3V',
                                                        'A5V','F0V','F2V','F5V','G0V','G2V',
                                                        'G5V','K0V','K2V','K5V','K7V','M0V',
                                                        'M2V','M3V','M4V','M5V','M6V',
                                                        'lyaem1', 'lyaem2', 'lyaem3', 'lyaem4'])
                    CRVAL3 = wx.StaticText(panel, label="Start lambda [A]:")
                    self.CRVAL3VAL = wx.TextCtrl(panel, value="5000.0")
                    SPECEND=wx.StaticText(panel, label="End lambda [A]:")
                    self.SPECENDVAL = wx.TextCtrl(panel, value="8000.0")
                    R = wx.StaticText(panel, label="Resolving power:")
                    self.RVAL = wx.TextCtrl(panel, value="1000")
                    MAG = wx.StaticText(panel, label="AB Mag:")
                    self.MAGVAL = wx.TextCtrl(panel, value="20.0")
                    BAND = wx.StaticText(panel, label="Band:")
                    self.BANDVAL = wx.Choice(panel, choices=['V', 'R', 'I', 'z', 'J', 'H', 'K', 'L', 'M'])
                    Z = wx.StaticText(panel, label="Redshift:")
                    self.ZVAL = wx.TextCtrl(panel, value="0.1")
                    
                    fg.AddMany([(subspect), (spect),
                                (INPUTSPEC),(self.INPUTSPECVAL, 1, wx.EXPAND),
                                (USERRES), (self.USERRESVAL, 1, wx.EXPAND),
                                (orlabel), (suborlabel),
                                (SPECTRA), (self.SPECTRAVAL, 1, wx.EXPAND),
                                (CRVAL3), (self.CRVAL3VAL, 1, wx.EXPAND),
                                (SPECEND), (self.SPECENDVAL, 1, wx.EXPAND),
                                (R), (self.RVAL, 1, wx.EXPAND),
                                (MAG), (self.MAGVAL, 1, wx.EXPAND),
                                (BAND), (self.BANDVAL, 1, wx.EXPAND),
                                (Z), (self.ZVAL, 1, wx.EXPAND),])
                    
                    fg.AddGrowableCol(1,1)

                    hbox.Add(fg, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
                       
                    #Spatial Parameters
                    fgs = wx.FlexGridSizer(11, 2, 15, 10)

                    spat = wx.StaticText(panel, label='Spatial Parameters')
                    spat.SetFont(titlefont)
                    subspat = wx.StaticText(panel, label=' ')
                    CDELT1 = wx.StaticText(panel, label="Spaxel scale [mas]:")
                    self.CDELT1VAL = wx.TextCtrl(panel, value="1")
                    NUMSPAX = wx.StaticText(panel, label="FoV [spaxels]:")
                    self.NUMSPAXVAL = wx.TextCtrl(panel, value="500")
                    OBJTYPE = wx.StaticText(panel, label="Object Type:")
                    self.OBJTYPEVAL = wx.Choice(panel, choices=['Point','Galaxy'])
                    NUMGAL = wx.StaticText(panel, label="Number of Objects:")
                    self.NUMGALVAL = wx.Choice(panel, choices=['1', '2'])
                    PIXSEP = wx.StaticText(panel, label="Object Sep (if two) [spaxels]:")
                    self.PIXSEPVAL = wx.TextCtrl(panel, value="10")
                    FAC = wx.StaticText(panel, label="Brightness Offset (if two):")
                    self.FACVAL = wx.TextCtrl(panel, value="1.5")
                    # KN = wx.StaticText(panel, label="Galaxy Sersic Parameters:")
                    K = wx.StaticText(panel, label="Sersic k (if Galaxy):")
                    self.KVAL= wx.TextCtrl(panel, value="10.")
                    N= wx.StaticText(panel, label="Sersic n (if Galaxy):")
                    self.NVAL= wx.TextCtrl(panel, value="0.65")

                    fgs.AddMany([(subspat), (spat),
                                 (CDELT1), (self.CDELT1VAL, 1, wx.EXPAND),
                                 (NUMSPAX), (self.NUMSPAXVAL, 1, wx.EXPAND),
                                 (OBJTYPE), (self.OBJTYPEVAL, 1, wx.EXPAND),
                                 (NUMGAL), (self.NUMGALVAL, 1, wx.EXPAND),
                                 (PIXSEP), (self.PIXSEPVAL, 1, wx.EXPAND),
                                 (FAC), (self.FACVAL, 1, wx.EXPAND),
                                 (K), (self.KVAL, 1, wx.EXPAND),
                                 (N), (self.NVAL, 1, wx.EXPAND)])
                    
                    fgs.AddGrowableCol(1,1)

                    hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)
                    
                    #Misc. parameters
                    fgss = wx.FlexGridSizer(11, 2, 15, 10)

                    misc = wx.StaticText(panel, label="Extra Parameters")
                    misc.SetFont(titlefont)
                    submisc = wx.StaticText(panel, label=' ')
                    LINETEXT = wx.StaticText(panel, label="Emission line")
                    LINETEXT.SetFont(subtitlefont)
                    gapline = wx.StaticText(panel, label="(if 'Emission' chosen)")
                    GAUSSWAVE = wx.StaticText(panel, label="Wavelength [A]:")
                    self.GAUSSWAVEVAL = wx.TextCtrl(panel, value="0.")
                    GAUSSWIDTH = wx.StaticText(panel, label="Width [km/s]:")
                    self.GAUSSWIDTHVAL = wx.TextCtrl(panel, value="20.")
                    GAUSSFLUX = wx.StaticText(panel, label="Total flux [erg/s/cm2]:")
                    self.GAUSSFLUXVAL = wx.TextCtrl(panel, value="1E-16")
                    gapaa = wx.StaticText(panel, label=' ------------ ')
                    gapbb = wx.StaticText(panel, label=' ')
                    DIR = wx.StaticText(panel, label='Output Directory')
                    DIR.SetFont(subtitlefont)
                    gapdir = wx.StaticText(panel, label=' ')
                    self.DIRVAL = wx.DirPickerCtrl(panel, path=path_setup('../Output_cubes/'))
                    NAME = wx.StaticText(panel, label="File Name")
                    NAME.SetFont(subtitlefont)
                    gapname = wx.StaticText(panel, label=' ')
                    self.NAMEVAL = wx.TextCtrl(panel, value="New_datacube")

                    fgss.AddMany([(submisc), (misc),
                                  (LINETEXT), (gapline),
                                  (GAUSSWAVE), (self.GAUSSWAVEVAL, 1, wx.EXPAND),
                                  (GAUSSWIDTH), (self.GAUSSWIDTHVAL, 1, wx.EXPAND),
                                  (GAUSSFLUX), (self.GAUSSFLUXVAL, 1, wx.EXPAND),
                                  (gapaa), (gapbb),
                                  (DIR), (self.DIRVAL, 1, wx.EXPAND),
                                  (NAME), (self.NAMEVAL, 1, wx.EXPAND)])

                    fgss.AddGrowableCol(1,1)

                    hbox.Add(fgss, proportion=1, flag=wx.ALL|wx.EXPAND, border=10)

                    panel.SetSizer(hbox)

                    # A button
                    button =wx.Button(panel, 10, "Generate Cube", wx.Point(475, 340))
                    wx.EVT_BUTTON(panel, 10, self.OnClick)

                def OnClick(self,event):
                    #Extract parameters for FITS header:
                    cdelt1=float(self.CDELT1VAL.GetValue())
                    crval3=float(self.CRVAL3VAL.GetValue())
                    specend=float(self.SPECENDVAL.GetValue())
                    R=float(self.RVAL.GetValue())

                    #Extract model parameters
                    userspec = str(self.INPUTSPECVAL.GetPath())
                    userres = float(self.USERRESVAL.GetValue())
                    numgal=int(self.NUMGALVAL.GetStringSelection())
                    fov=int(self.NUMSPAXVAL.GetValue())
                    source_type=str(self.OBJTYPEVAL.GetStringSelection())
                    zval=float(self.ZVAL.GetValue())
                    ABmag=float(self.MAGVAL.GetValue())
                    bandval=str(self.BANDVAL.GetStringSelection())
                    source_sep=int(self.PIXSEPVAL.GetValue())
                    brightness_offset=float(self.FACVAL.GetValue())
                    spectype=str(self.SPECTRAVAL.GetStringSelection())
                    linewave=float(self.GAUSSWAVEVAL.GetValue())
                    linewidth=float(self.GAUSSWIDTHVAL.GetValue())
                    lineflux=float(self.GAUSSFLUXVAL.GetValue())
                    name=str(self.NAMEVAL.GetValue())
                    sersic_k=float(self.KVAL.GetValue())
                    sersic_n=float(self.NVAL.GetValue())
                    odir = str(self.DIRVAL.GetPath())

                    #Collect parameters into lists
                    crpix3 = 1               #CRPIX1
                    cunit1 = 'mas'           #CUNIT1
                    cunit2 = 'mas'           #CUNIT2
                    cunit3 = 'angstroms'     #CUNIT3
                    ctype1 = 'RA'            #CTYPE1
                    ctype2 = 'DEC'           #CTYPE2
                    ctype3 = 'WAVELENGTH'    #CTYPE3
                    specr = R                #RPOWER
                    funits = 'erg/s/cm2/A/arcsec2/'
                    centre = 1
                    grid = 1
                    headerdata = [cdelt1, cdelt1, crval3, specend, R,
                    funits, crpix3, cunit1, cunit2, cunit3, ctype1, ctype2, ctype3]
                    modeldata = [numgal, fov, fov, source_type, zval, ABmag, bandval,
                    source_sep, brightness_offset, spectype, linewave, linewidth, lineflux, centre, grid,
                    name, sersic_k, sersic_n]
                    #Start main program
                    main.main(headerdata, modeldata, userspec, userres, odir)

                def OnExit(self,e):
                    self.Close(True)  # Close the frame.

                def OnAbout(self,e):
                    info = wx.AboutDialogInfo()
                    #info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
                    info.SetName('CUBEGEN')
                    info.SetVersion(ver)
                    info.SetDescription('Data cube Generation pipeline')
                    #info.SetCopyright('(C) 2014')
                    info.SetWebSite('https://github.com/szieleniewski/CUBEGEN')
                    #info.SetLicence(licence)
                    info.AddDeveloper('Simon Zieleniewski, Nicholas Zieleniewski & Sarah Kendrew')
                    info.AddDocWriter('Simon Zieleniewski')
                    #info.AddArtist('Artist')
                    #info.AddTranslator('Translator')
                    wx.AboutBox(info)

        except:
            print""
            print 'CUBEGEN Input Data Cube Generator'
            print '    --------     '
            print 'NO WX MODULE'
            print 'wxPython can be downloaded from: http://www.wxpython.org/'
            print""
            print 'COMMAND LINE USAGE ONLY'
            print""
            print '>>> python cubegen.py -c arg1 arg2 ...'
            print""
            print 'To see help:'
            print""
            print '>>> python cubegen.py -c -h'
            print""
            print 'To see required arguments:'
            print""
            print '>>> python cubegen.py -c'
            print""
            print"---"
            sys.exit()
        if wxfound:
            #GUI interface
            app = wx.App()
            Form1(None, title="CUBEGEN Generator Interface")
            app.MainLoop()
