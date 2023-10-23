# ConversionCalculator (v1.19.1)
# Python 3.9.6
# A program by Tyler Serio
# This program converts units to other units

# Import packages
import tkinter
import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Define important unit dictionaries in terms of SI units
# https://en.wikipedia.org/wiki/List_of_conversion_factors
# Acceleration units dictionary
acceldict = {
    "Feet per Hour per Second (fph/s)": 0.000084666666,
    "Feet per Minute per Second (fpm/s)": 0.00508,
    "Feet per Second Squared (fps^2)": 0.3048,
    "Gals, Galileos (Gal)": 0.01,
    "Inches per Minute per Second (ipm/s)": 0.00042333333,
    "Inches per Second Squared (ips^2)": 0.0254,
    #"Knots per Second (kn/s)": ,
    "Meters per Second Squared (m/s^2)": 1,
    "Miles per Hour per Second (mph/s)": 0.44704,
    "Miles per Minute per Second (mpm/s)": 26.8224,
    "Miles per Second Squared (mps^2)": 1609.344,
    "Standard Gravity (g0)": 9.80665
    }

# Alcohol units dictionary
# Drink responsibly
alcoholdict = {
    "10mls or 8gs of Pure Alcohol": 1,
    "440ml Cans of ABV 5.5% Lager/Beer/Cider": 2.4,
    "Units of Alcohol": 1,
    "Pints of ABV 3.6% Lager/Beer/Cider": 2,
    "Pints of ABV 5.2% Lager/Beer/Cider": 3,
    "British Weekly Recommended Limit": 14,
    "25ml Single Small Shots of Spirits, ABV 40%": 1
    }

# Density units dictionary
densitydict = {
    "Grams per Mililiter (g/mL)": 1000,
    "Kilograms per Cubic Meter (kg/m^3)": 1,
    "Kilograms per Liter (kg/L)": 1000,
    "Avoirdupois Ounces per Cubic Foot (oz/ft^3)": 1.001153961,
    "Avoirdupois Ounces per Cubic Inch (oz/in^3)": 1.729994044,
    "Avoirdupois Ounces per Imperial Gallon (oz/gal)":  6.236023291,
    "Avoirdupois Ounces per US Fluid Gallon (oz/gal)": 7.489151707,
    "Avoirdupois Pounds per Foot (lb/ft^3)": 16.01846337,
    "Avoirdupois Pounds per Inch (lb/in^3)":  2.767990471,
    "Avoirdupois Pounds per Imperial Gallon (lb/gal)": 99.77637266,
    "Avoirdupois Pounds per US Fluid Gallon (lb/gal)": 119.8264273,
    "Slugs per Cubic Foot (slug/ft^3)": 515.3788184
    }

# Energy units dictionary
energydict = {
    "Calories, US;FDA (Cal)": 4184,
    "Electronvolt (eV)": 0.0000000000000000001602176634,
    "Joules (J)": 1,
    "Kilocalories, Large Calories (kcal; Cal)": 4186.8,
    "Quads": 1055055852620000000,
    "Tonnes of Coal Equivalent (TCE)": 29288000000,
    "Tonnes of Oil Equivalent (toe)": 41840000000,
    "Tons of TNT (tTNT)": 4184000000
    }

# Frequency units dictionary
freqdict = {
    "Actions per Minute (APM)": 1/60,
    "Cycles per Second (cps)": 1,
    "Degrees per Second (deg/s)": 0.00277777,
    "Hertz (Hz)": 1,
    "Radians per Second (rad/s)": 0.159155,
    "Revolutions per Minute (rpm)": 1/60
    }

# Force units dictionary
forcedict = {
    "Atomic Units of Force": 0.0000000823872206,
    "Dynes, CGS Unit (dyn)": 0.00001,
    #"Kilogram-Force, Kiloponds, Grave-Force (kgf; kp; gvf)": ,
    "Kips, Kip-Force (kip; kipf; klbf)":  4448.2216152605,
    #"Milligrave-Force, Gravet-Force (mgvf; gvtf)": 0.00980665,
    "Long Tons-Force (tnf)": 9964.01641818352,
    "Newtons (N)": 1,
    "Ounces-Force (ozf)": 0.27801385095378125,
    "Pounds-Force (lbf)": 4.4482216152605,
    "Poundals (pdl)": 0.138254954376,
    "Short Tons-Force (tnf)": 8896.443230521,
    "Sthenes (sn)": 1000
    }

# Information entropy units dictionary
infoendict = {
    "Bits (b)": 1,
    "Bytes (B)": 8,
    "Nibbles": 4,
    "Kilobytes (kB)": 8000,
    "Kibibytes (Kib)": 8192,
    "Shannons (Sh)": 1
    }

# Length units dictionary
lengthdict = {
    "Ångströms (Å)": .0000000001,
    "Astronomical Units (au)": 149597870700,
    "Attometers (am)": 0.000000000000000001,
    "Barelycorns, H": 0.00846,
    "Cable Lengths, Imperial": 185.3184,
    "Cable Lengths, International": 185.2,
    "Centimeters (cm)": 0.01,
    "Decameters (dam)": 10,
    "Decimeters (dm)": 0.1,
    "Ells, H (ell)": 1.143,
    "Fathoms (ftm)": 1.8288,
    "Feet, International (ft)": 0.3048,
    "Femtometers (fm)": 0.000000000000001,
    "Fingers": 0.022225,
    "Hectometers (hm)": 100,
    "Inches, International (in)": 0.0254,
    "Kilometers (km)": 1000,
    "Light-Days": 25902068371200,
    "Light-Hours": 1079252848800,
    "Light-Seconds": 299792458,
    "Light-Years": 9460730472580800,
    "Lines (ln)": 0.0021166666,
    "Meters (m)": 1,
    "Micrometers, Microns (μm)": 0.000001,
    "Miles, Internaional (mi)": 1609.344,
    "Millimeters (mm)": 0.001,
    "Nanometers (nm)": 0.000000001,
    "Nautical Miles, International (nmi)": 1852,
    "Paces": 0.762,
    "Palms": 0.0762,
    "Parsecs (pc)": 30856775814913700,
    "Picometers (pm)": 0.000000000001,
    "Quarters": 0.2286,
    "Scandinavian Miles (mil)": 10000,
    "Spans, H": 0.2286,
    "Spats":1000000000000,
    "Sticks, H": 0.0508,
    "Twips (twp)": 0.00001763888888,
    "Yards, International (yd)": 0.9144,
    "Yoctommeters (ym)": 0.000000000000000000000001,
    "Zeptometers (zm)": 0.000000000000000000001
    }

# Temperature units dictionary
tempdict = {
    "Degrees Celsius (°C)": ["x - 273.15", "x + 273.15"],
    "Degrees Delisle (°De)": ["(373.15 - x) * (3 / 2)", "373.15 - (x * (2 / 3))"],
    #"Degrees Fahrenheit (°F)": "",
    #"Degrees Newton (°N)": "",
    "Degrees Rankine (°R)": ["x /(5/9)", "x * (5/9)"],
    #"Degrees Réaumur (°Ré)": "",
    #"Degrees Rømer (°Rø)": ,
    #"Regulo Gas Marks (GM)": "",
    "Kelvins (K)": ["x", "x"]
    }

# Time units dictionary
timedict = {
    "Days (d)": 86400,
    "Hours (h)": 3600,
    "Jiffies (j)": 1/60,
    "Jiffies, Alternative (ja)": 0.01,
    "Kès, Quarters of an Hour": 900,
    "Kès, Traditional": 864,
    "Millenniums": 31536000000,
    "Millidays (md)": 86.4,
    "Minutes (min)": 60,
    "Moments": 90,
    "Seconds (s)": 1,
    "Shakes": 0.00000001,
    "Sigmas": 0.000001,
    "Svedbergs": 0.0000000000001,
    "Weeks (wk)": 604800,
    "Years, Common (y)": 31536000
    }

# Mass units dictionary
massdict = {
    "Bags, Coffee": 60,
    "Bags, Portland Cement": 42.63768278,
    "Barges": 20411.65665,
    "Carats, Metric (ct)": 0.0002,
    "Cloves": 3.62873896,
    "Grains (gr)": 0.00006479891,
    "Grams (g)": 0.001,
    "Graves (gv)": 1,
    "Kilograms (kg)": 1,
    "Kips, (kip)": 453.59237,
    "Mites": 0.00005,
    "Ounces, Avoirdupois (oz av)": 0.028349523125,
    "Pounds, Avoirdupois (lb av)": 0.45359237,
    "Quintals, Metric (q)": 100,
    "Scruples, Apothecary (s ap)": 0.0012959782,
    "Stones (st)": 6.35029318,
    "Tonnes,MTS Unit (t)": 1000,
    "Weys": 114.30527724
    }

# Volume units dictionary
volumedict = {
    "Cubic Meters (m^3)": 1,
    "Cubic Miles (cu mi)": 4168181825.440579584,
    "Cubic Yards (yd^3)": 0.764554857984,
    "Cups, Metric (c)": 0.00025,
    "Liters (L)": 0.001,
    "Petroleum Barrels, Archaic Blue-Barrels": 0.158987294928
    }

# Define unit lists from dictionary keys
accellist = []
alcohollist = []
densitylist = []
energylist = []
forcelist = []
freqlist = []
infoenlist = []
lengthlist = []
masslist = []
templist = []
timelist = []
volumelist = []
listoflists = [accellist, alcohollist, densitylist, energylist, forcelist, freqlist, infoenlist, lengthlist, templist, timelist, masslist, volumelist]
listofdicts = [acceldict, alcoholdict, densitydict, energydict, freqdict, forcedict, infoendict, lengthdict, tempdict, timedict, massdict, volumedict]
xdict = -1
for xlist in listoflists:
    xdict += 1
    for key in listofdicts[xdict].keys():
        xlist.append(str(key))

# Unit type dictionary
typedict = {
    "Acceleration": [acceldict, accellist, "Meters per Second Squared (m/s^2)", "Gals, Galileos (Gal)"],
    "Alcohol": [alcoholdict, alcohollist, "Units of Alcohol", "10mls or 8gs of Pure Alcohol"],
    "Density": [densitydict, densitylist, "Kilograms per Cubic Meter (kg/m^3)", "Grams per Mililiter (g/mL)"],
    "Energy": [energydict, energylist, "Joules (J)", "Calories, US;FDA (Cal)"],
    "Force": [forcedict, forcelist, "Newtons (N)", "Atomic Units of Force"],
    "Frequency": [freqdict, freqlist, "Hertz (Hz)", "Actions per Minute (APM)"],
    "Information Entropy": [infoendict, infoenlist, "Bits (b)", "Bytes (B)"],
    "Length": [lengthdict, lengthlist, "Meters (m)", "Inches, International (in)"],
    "Mass": [massdict, masslist, "Kilograms (kg)", "Pounds, Avoirdupois (lb av)"],
    "Temperature": [tempdict, templist, "Kelvins (K)", "Degrees Celsius (°C)"],
    "Time": [timedict, timelist, "Seconds (s)", "Jiffies (j)"],
    "Volume": [volumedict, volumelist, "Cubic Meters (m^3)", "Cubic Yards (yd^3)"]
    }

# Define list of unit types
typelist = []
for key in typedict.keys():
    typelist.append(str(key))
typelist.append("[Help Menu]")
typelist.append("[Exit]")

# Define important functions
# Create function to change unit variable
def changevar(unit):
    global gunit
    global default1
    global default2
    global default3
    global unitlist
    global omenu1
    global omenu2
    global omenu3
    global var1
    global var2
    global unit1
    global unit2
    gunit = unit

    if gunit == "[Exit]":
        exit()

    # Help menu pops up when option selected
    if gunit == "[Help Menu]":
        helpbox()
        gunit = "Acceleration"
        omenu3.destroy()
        default3.set("Acceleration")
        omenu3 = OptionMenu(frm2,  default3, *typelist, command=changevar)
        omenu3.grid(column=2, row=7, pady = 3)

    unitlist = typedict[gunit][1]
    x = typedict[gunit][2]
    y = typedict[gunit][3]
        
    dictionary = typedict[gunit][0]
    default1.set(x)
    unit1 = dictionary[x]

    if gunit == "Temperature":
        default2.set(y)
        x = 1
        var2 = eval(dictionary[y][0])
        unit1 = unit1[0]
        unit2 = dictionary[y][0]

    else:
        default2.set(y)
        var2 = 1 / dictionary[y]
        unit2 = dictionary[y]    
        
    var1 = 1.0
    
    omenu1.destroy()
    omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1)
    omenu1.config(width=42)
    omenu1.grid(column=1, row=5, padx = 2)
    
    omenu2.destroy()
    omenu2 = OptionMenu(frm, default2, *unitlist, command=callback2)
    omenu2.config(width=42)
    omenu2.grid(column=4, row=5, padx = 2)

    replaceentries(var1, var2)
    
# Function that calculates unit conversion
def calcvar():
    global var1
    global var2
    
    var1 = float(entry1.get())

    if gunit == "Temperature":
        x = var1
        x = eval(unit1)
        var2 = eval(unit2)
    else:
        var2 = (var1 * unit1) / unit2
        
    replaceentries(var1, var2)

# Function that changes entry boxes to reflect unit conversions
def replaceentries(varone, vartwo):
    global entry1
    global entry2
    
    entry1.destroy()
    entry1 = ttk.Entry(frm, width=24)
    entry1.insert(END, str(varone))
    entry1.grid(column=0, row=5, padx = 2)

    entry2.destroy()
    entry2 = ttk.Entry(frm, width=24)
    entry2.insert(END, str(vartwo))
    entry2.grid(column=3, row=5, padx = 2)
    
    root.update()

# Function to change first unit 
def callback1(selection):
    global unit1
    xdict = typedict[gunit][0]
    if gunit == "Temperature":
        unit1 = xdict[selection][1]
    else:
        unit1 = xdict[selection]
    calcvar()

# Function to change second unit
def callback2(selection):
    global unit2
    xdict = typedict[gunit][0]
    if gunit == "Temperature":
        unit2 = xdict[selection][0]
    else:   
        unit2 = xdict[selection]
    calcvar()

# Create a window for the help menu
def helpbox():
    helpbox = Toplevel(root)
    helpbox.geometry("+" + str(int(0.1 * screen_width)) + "+" + str(int(0.2 * screen_height)))
    root.resizable(False, False)
    helpbox.focus_set()
    helpbox.grab_set()
    helpbox.title("Help!")
    imagename = "icons8-weight-90.png"
    image = PhotoImage(file = imagename)
    root.iconphoto(False, image)
    frm = ttk.Frame(helpbox, padding=5)
    frm.grid()
    ttk.Label(frm, text="This is the help menu... Currently you are on your own!").grid(column=0, row=0)

# Get monitor dimensions
screen_width = pyautogui.size()[0]
screen_height = pyautogui.size()[1]

# Define the root window
root = Tk()
root.geometry("+" + str(int(0.1 * screen_width)) + "+" + str(int(0.2 * screen_height)))
root.resizable(False, False)
root.title("ConversionCalculator (v1.19.1)")
imagename = "icons8-weight-90.png"
image = PhotoImage(file = imagename)
root.iconphoto(False, image)
frm = ttk.Frame(root, padding=5)
frm2 = ttk.Frame(root, padding=5)

# Call grid method for frames
frm.grid()
frm2.grid()
    
# Define first unit for conversion
gunit = "Acceleration"
var1 = 1.0
var2 = acceldict["Meters per Second Squared (m/s^2)"] / acceldict["Gals, Galileos (Gal)"]
unit1 = 1
unit2 = .01
unitlist = accellist
unitlist = unitlist

# Set default selections for the options menus
default1 = StringVar(frm)
default1.set("Meters per Second Squared (m/s^2)")

default2 = StringVar(frm)
default2.set("Gals, Galileos (Gal)")

default3 = StringVar(frm2)
default3.set("Acceleration")

# Define first entry for number of units
entry1 = ttk.Entry(frm, width=24)
entry1.insert(END, var1)
entry1.grid(column=0, row=5, padx = 2)

# Define the first option menu for choosing conversion units
omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1)
omenu1.config(width=42)
omenu1.grid(column=1, row=5, padx = 2)

# Define label to aid in understanding of unit conversion
islabel = ttk.Label(frm, text=f"is equal to ")
islabel.grid(column=2, row=5, padx = 2)

# Define second entry for number of units
entry2 = ttk.Entry(frm, width=24)
entry2.insert(END, str(var2))
entry2.grid(column=3, row=5, padx = 2)

# Define the second option menu for choosing conversion units
omenu2 = OptionMenu(frm, default2, *unitlist, command=callback2)
omenu2.config(width=42)
omenu2.grid(column=4, row=5, padx = 2)

# Define the calculate button
calcbtt = ttk.Button(frm2, text="Calculate", command=calcvar)
calcbtt.grid(column=1, row=7, pady = 3)

# Define the option menu for selecting unit types
omenu3 = OptionMenu(frm2, default3, *typelist, command=changevar)
omenu3.grid(column=2, row=7, pady = 3)

# Mainloop
root.mainloop()
