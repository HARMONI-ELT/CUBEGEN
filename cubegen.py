'''code contianing GUI and command line options
for data cube generation interface for HSIM
(or general input datacubes)

Author: Simon Zieleniewski & Nicholas Zieleniewski

Last updated: 30-09-16

'''


import wx
from Modules import main
from Modules import spectra as sp


# class Form1(wx.Frame):
	
# 	def __init__(self, parent, title):
# 			super(Form1, self).__init__(parent, title=title, 
#             size=(1120, 390))

#             self.InitUI()
#             self.Centre()
#             self.Show()

# 	def InitUI(self):

#         panel = wx.Panel(self)
#         titlefont = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)

#         # Set up the menu.
#         filemenu  = wx.Menu()
#         menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
#         menuExit  = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

#         # Creating the menubar.
#         menuBar = wx.MenuBar()
#         menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
#         self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

#         # Events.
#         self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
#         self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        
#         hbox = wx.BoxSizer(wx.HORIZONTAL)

#         fg = wx.FlexGridSizer(8, 2, 15, 10)

class Form1(wx.Panel):

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)

        # INPUTSPEC = wx.StaticText(panel, label="Input spectrum file")
        # self.INPUTSPECVAL = wx.FilePickerCtrl(panel, path="")

        #Enter parameters for FITS header (and others)
        self.CDELT1 = wx.StaticText(self, -1, "Spaxel X [arcsec]:",wx.Point(20,20))
        self.CDELT1VALUE = wx.TextCtrl(self, 20, "0.010", wx.Point(160, 20), wx.Size(120,-1))
        self.CDELT2 = wx.StaticText(self, -1, "Spaxel Y [arcsec]:",wx.Point(20,50))
        self.CDELT2VALUE = wx.TextCtrl(self, 30, "0.010", wx.Point(160,50), wx.Size(120,-1))
        self.CRVAL3 = wx.StaticText(self, -1, "Initial lambda [A]:",wx.Point(20,80))
        self.CRVAL3VALUE = wx.TextCtrl(self, 50, "7300.0", wx.Point(160,80), wx.Size(120,-1))
        self.SPECEND=wx.StaticText(self, -1, "Max lambda [A]:",wx.Point(20,110))
        self.SPECENDVAL = wx.TextCtrl(self, 20, "15000.0", wx.Point(160, 110), wx.Size(120,-1))
        self.R = wx.StaticText(self, -1, "Resolving power:",wx.Point(20,140))
        self.RVALUE = wx.TextCtrl(self, 20, "1000", wx.Point(160, 140), wx.Size(120,-1))
        #self.FUNITS=wx.StaticText(self, -1, "FUNITS:",wx.Point(20,170))
        #self.FUNITSVALUE = wx.Choice(self, -1, wx.Point(100,170),choices=['J/s/m2/A/arcsec2','erg/s/cm2/A/arcsec2'])
        self.HRFACTOR = wx.StaticText(self, -1, "HRFACTOR:",wx.Point(20,200))
        self.HRFACTORVALUE = wx.TextCtrl(self, 60, "1", wx.Point(160,200), wx.Size(120,-1))
        self.NAME = wx.StaticText(self, -1, "File Name: ",wx.Point(20,230))
        self.NAMEVAL = wx.TextCtrl(self, -1, "Datacube",wx.Point(160,230),wx.Size(120,-1))

        #Enter galaxy model parameters:
        self.NUMGAL = wx.StaticText(self, -1, "Number of Objects:",wx.Point(300,20))
        self.NUMGALVALUE = wx.TextCtrl(self, 20, "1", wx.Point(450, 20), wx.Size(100,-1))
        self.OBJTYPE = wx.StaticText(self, -1, "Object Type:",wx.Point(300,50))
        self.OBJTYPEVALUE = wx.Choice(self, wx.ID_ANY, wx.Point(450,50),choices=['Point','Galaxy'])
        self.OBJTYPEVALUE.SetSelection(0)
        self.NUMSPAX = wx.StaticText(self, -1, "Number of Spaxels:",wx.Point(300,80))
        self.NUMSPAXVALUE1 = wx.TextCtrl(self, 20, "128", wx.Point(450, 80), wx.Size(35,-1))
        self.NUMSPAX2 = wx.StaticText(self, -1, " x ",wx.Point(490,85))
        self.NUMSPAXVALUE2 = wx.TextCtrl(self, 20, "256", wx.Point(515, 80), wx.Size(35,-1))
        self.Z = wx.StaticText(self, -1, "Redshift:",wx.Point(300,110))
        self.ZVALUE = wx.TextCtrl(self, 20, "0.1", wx.Point(450, 110), wx.Size(100,-1))
        self.MAG = wx.StaticText(self, -1, "AB Mag:",wx.Point(300,170))
        self.MAGVALUE = wx.TextCtrl(self, 20, "20.0", wx.Point(450, 170), wx.Size(100,-1))
        self.BAND = wx.StaticText(self, -1, "Band:",wx.Point(300,200))
        self.BANDVALUE = wx.Choice(self, wx.ID_ANY, wx.Point(450,200),
                                      choices=['V', 'R', 'I', 'z', 'J', 'H', 'K',
                                               'L', 'M'])
        self.SPECTRA = wx.StaticText(self, -1, "Spectrum Type:", wx.Point(300,230))
        self.SPECTRAVALUE = wx.Choice(self, wx.ID_ANY, wx.Point(430,230),
                                      choices=['Flat','Emission','Absorption','O5V',
                                               'O9V','B0V','B3V','B9V','A0V','A3V',
                                               'A5V','F0V','F2V','F5V','G0V','G2V',
                                               'G5V','K0V','K2V','K5V','K7V','M0V',
                                               'M2V','M3V','M4V','M5V','M6V',
                                               'lyaem1', 'lyaem2', 'lyaem3', 'lyaem4'])
        self.SPECTRAVALUE.SetSelection(0)
##        self.BREAKFAC = wx.StaticText(self, -1, "Flux Reduction Factor:", wx.Point(300,230))
##        self.BREAKFACTORVAL = wx.TextCtrl(self, 20, "4.", wx.Point(450, 230), wx.Size(100,-1))
        self.CURVEINFO = wx.StaticText(self, -1, "Emission line:",wx.Point(590,140))
        self.GAUSSWAVE = wx.StaticText(self, -1, "Wavelength [A]:",wx.Point(580,170))
        self.GAUSSWAVEVALUE = wx.TextCtrl(self, 20, "0.", wx.Point(730, 170), wx.Size(80,-1))
        self.GAUSSWIDTH = wx.StaticText(self, -1, "Width [km/s]:",wx.Point(580,200))
        self.GAUSSWIDTHVALUE = wx.TextCtrl(self, 20, "20.", wx.Point(730, 200), wx.Size(80,-1))
        self.GAUSSFLUX = wx.StaticText(self, -1, "Total flux [erg/s/cm2]:",wx.Point(580,230))
        self.GAUSSFLUXVALUE = wx.TextCtrl(self, 20, "1e-16", wx.Point(730, 230), wx.Size(80,-1))

        #Misc parameters:
        self.MISC = wx.StaticText(self, -1, "Misc. Model Parameters",wx.Point(830,20))
        self.CENTREVALUE = wx.CheckBox(self, -1, "Centre galaxy image",wx.Point(830,50))
##        self.CIRCLEVALUE = wx.CheckBox(self, -1, "Apply circle shape",wx.Point(830,80))
##        self.LIM= wx.StaticText(self, -1, "Circle Radius:",wx.Point(830,110))
##        self.LIMVALUE= wx.TextCtrl(self, 20, "0.5", wx.Point(930, 110), wx.Size(35,-1))
        self.GRID= wx.StaticText(self, -1, "Grid Size:",wx.Point(830,140))
        self.GRIDVALUE= wx.TextCtrl(self, 20, "1", wx.Point(930, 140), wx.Size(35,-1))

        #Sersic profile parameters:
        self.KN = wx.StaticText(self, -1, "Galaxy Sersic Parameters:",wx.Point(830,170))
        self.K = wx.StaticText(self, -1, "k:",wx.Point(860,200))
        self.KVAL= wx.TextCtrl(self, 20, "10.", wx.Point(880, 200), wx.Size(60,-1))
        self.N= wx.StaticText(self, -1, "n:",wx.Point(860,230))
        self.NVAL= wx.TextCtrl(self, 20, "0.65", wx.Point(880, 230), wx.Size(60,-1))

        #Optional parameters for 2 galaxies:
        self.INFO = wx.StaticText(self, -1, "Parameters for 2 Galaxies",wx.Point(590,20))
        self.PIXSEP = wx.StaticText(self, -1, "Object Sep (pixels):",wx.Point(580,50))
        self.PIXSEPVALUE = wx.TextCtrl(self, 20, "10", wx.Point(730, 50), wx.Size(50,-1))
        self.FAC = wx.StaticText(self, -1, "Brightness Offset:",wx.Point(580,80))
        self.FACVALUE = wx.TextCtrl(self, 20, "1.5", wx.Point(730, 80), wx.Size(50,-1))

        # A button
        self.button =wx.Button(self, 10, "Generate Datacube", wx.Point(450, 270))
        wx.EVT_BUTTON(self, 10, self.OnClick)

    def OnClick(self,event):
        #Extract parameters for FITS header:
        cdelt1=float(self.CDELT1VALUE.GetValue())
        cdelt2=float(self.CDELT2VALUE.GetValue())
        crval3=float(self.CRVAL3VALUE.GetValue())
        specend=float(self.SPECENDVAL.GetValue())
        R=float(self.RVALUE.GetValue())
        #funits=str(self.FUNITSVALUE.GetStringSelection())
        hrfac=float(self.HRFACTORVALUE.GetValue())

        #Extract model parameters
        numgal=int(self.NUMGALVALUE.GetValue())
        xnumspax=int(self.NUMSPAXVALUE1.GetValue())
        ynumspax=int(self.NUMSPAXVALUE2.GetValue())
        otype=str(self.OBJTYPEVALUE.GetStringSelection())
        zval=float(self.ZVALUE.GetValue())
        magval=float(self.MAGVALUE.GetValue())
        bandval=float(self.BANDVALUE.GetStringSelection())
        pixsep=int(self.PIXSEPVALUE.GetValue())
        facval=float(self.FACVALUE.GetValue())
        specval=str(self.SPECTRAVALUE.GetStringSelection())
        linewave=float(self.GAUSSWAVEVALUE.GetValue())
        linewidth=float(self.GAUSSWIDTHVALUE.GetValue())
        lineflux=float(self.GAUSSFLUXVALUE.GetValue())
        centre=self.CENTREVALUE.GetValue()
        grid=int(self.GRIDVALUE.GetValue())
        name=str(self.NAMEVAL.GetValue())
        kval=float(self.KVAL.GetValue())
        nval=float(self.NVAL.GetValue())

        crpix3 = 1               #CRPIX1
        cunit1 = 'mas'           #CUNIT1
        cunit2 = 'mas'           #CUNIT2
        cunit3 = 'angstroms'     #CUNIT3
        ctype1 = 'RA'            #CTYPE1
        ctype2 = 'DEC'           #CTYPE2
        ctype3 = 'WAVELENGTH'    #CTYPE3
        specr = R                #RPOWER
        funits = 'erg/s/cm2/A/arcsec2/'

        #collect parameters into lists
        headerdata = [cdelt1, cdelt2, crval3, specend, R, funits,
        crpix3, cunit1, cunit2, cunit3, ctype1, ctype2, ctype3, hrfac]
        modeldata = [numgal, xnumspax, ynumspax, otype, zval, magval, bandval,
        pixsep, facval, specval, linewave, linewidth, lineflux, centre, grid,
        name, kval, nval]
        #start main program
        main.main(headerdata, modeldata)


app = wx.PySimpleApp()
frame = wx.Frame(None, -1, "HSIM/NIFSIM Datacube Generator")
Form1(frame,-1)
frame.Size=(1010,330)
frame.Show(True)
app.MainLoop()
