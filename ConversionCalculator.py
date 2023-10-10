# ConversionCalculator (v1.10.1)
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
    "Gals, Galileos (Gal)": .01,
    "Inches per Minute per Second (ipm/s)": 0.00042333333,
    "Inches per Second Squared (ips^2)": 0.0254,
    #"Knots per Second (kn/s)": ,
    "Meters per Second Squared (m/s^2)": 1,
    "Miles per Hour per Second (mph/s)": 0.44704,
    "Miles per Minute per Second (mpm/s)": 26.8224,
    "Miles per Second Squared (mps^2)": 1609.344,
    "Standard Gravity (g0)": 9.80665
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
    #"Kips, Kip-Force (kip; kipf; klbf)": ,
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
    #"Hartley; Ban (Hart; ban)": ,
    #"Natural Unit of Information; Nit; Nepit (nat)": ,
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
    "Cable Lengths, International": 185.2,
    "Centimeters (cm)": 0.01,
    "Decameters (dam)": 10,
    "Decimeters (dm)": 0.1,
    "Feet, International (ft)": 0.3048,
    "Femtometers (fm)": 0.000000000000001,
    "Hectometers (hm)": 100,
    "Inches, International (in)": 0.0254,
    "Kilometers (km)": 1000,
    "Light-Days": 25902068371200,
    "Light-Hours": 1079252848800,
    "Light-Seconds": 299792458,
    "Light-Years": 9460730472580800,
    "Meters (m)": 1,
    "Micrometers, Microns (μm)": 0.000001,
    "Miles, Internaional (mi)": 1609.344,
    "Millimeters (mm)": 0.001,
    "Nanometers (nm)": 0.000000001,
    "Nautical Miles, International (nmi)": 1852,
    "Picometers (pm)": 0.000000000001,
    "Scandinavian Miles (mil)": 10000,
    "Spats":1000000000000,
    "Yards, International (yd)": 0.9144 
    }

# Temperature units dictionary
tempdict = {
    "Degrees Celsius(°C)": "x - 273.15",
    #"Degrees Delisle(°De)": "",
    #"Degrees Fahrenheit (°F)": "",
    #"Degrees Newton (°N)": "",
    "Degrees Rankine (°R)": "x/(5/9)",
    #"Degrees Réaumur (°Ré)": "",
    #"Degrees Rømer (°Rø)": ,
    #"Regulo Gas Marks (GM)": "",
    "Kelvins (K)": "x"
    }

# Time units dictionary
timedict = {
    "Days (d)": 86400,
    "Hours (h)": 3600,
    "Jiffies (j)": 1/60,
    "Jiffies, Alternative (ja)": 0.01,
    "Millenniums": 31536000000,
    "Minutes (min)": 60,
    "Moments": 90,
    "Seconds (s)": 1,
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

# Maybe add something list this later:
# listlist = [lengthlist, volumelist, etc.]
# for list in listlist:
#     list = []
#     for key in listdict.keys():
#     list.append(str(key))

# Define unit lists from dictionary keys
# Define Length unit list
lengthlist = []
for key in lengthdict.keys():
    lengthlist.append(str(key))

# Define Volume unit list
volumelist = []
for key in volumedict.keys():
    volumelist.append(str(key))

# Define Mass unit list
masslist = []
for key in massdict.keys():
    masslist.append(str(key))

# Define Time unit list
timelist = []
for key in timedict.keys():
    timelist.append(str(key))

# Define Frequency unit list
freqlist = []
for key in freqdict.keys():
    freqlist.append(str(key))

# Define Temperature unit list
templist = []
for key in tempdict.keys():
    templist.append(str(key))

# Define Information Entropy unit list
infoenlist = []
for key in infoendict.keys():
    infoenlist.append(str(key))

# Define Acceleration unit list
accellist = []
for key in acceldict.keys():
    accellist.append(str(key))

# Define Force unit list
forcelist = []
for key in forcedict.keys():
    forcelist.append(str(key))

# Unit type dictionary
typedict = {
    "Acceleration": [acceldict, accellist, "Meters per Second Squared (m/s^2)", "Gals, Galileos (Gal)"],
    "Force": [forcedict, forcelist, "Newtons (N)", "Atomic Units of Force"],
    "Frequency": [freqdict, freqlist, "Hertz (Hz)", "Actions per Minute (APM)"],
    "Information Entropy": [infoendict, infoenlist, "Bits (b)", "Bytes (B)"],
    "Length": [lengthdict, lengthlist, "Meters (m)", "Inches, International (in)"],
    "Mass": [massdict, masslist, "Kilograms (kg)", "Pounds, Avoirdupois (lb av)"],
    "Temperature": [tempdict, templist, "Kelvins (K)", "Degrees Celsius(°C)"],
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
    global unitlist
    global omenu1
    global omenu2
    global var1
    global var2
    global entry1
    global entry2
    global unit1
    global unit2
    gunit = unit

    if gunit == "[Exit]":
        exit()
    
    if gunit == "[Help Menu]":
        return        

    unitlist = typedict[gunit][1]
    x = typedict[gunit][2]
    y = typedict[gunit][3]
        
    dictionary = typedict[gunit][0]
    default1.set(x)
    unit1 = dictionary[x]

    if gunit == "Temperature":
        default2.set(y)
        x = 1
        var2 = eval(dictionary[y])
        unit2 = dictionary[y]

    else:
        default2.set(y)
        var2 = 1 / dictionary[y]
        unit2 = dictionary[y]    
        
    var1 = 1.0
    
    omenu1.destroy()
    omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1)
    omenu1.config(width=32)
    omenu1.grid(column=1, row=5, padx = 2)
    
    omenu2.destroy()
    omenu2 = OptionMenu(frm, default2, *unitlist, command=callback2)
    omenu2.config(width=32)
    omenu2.grid(column=4, row=5, padx = 2)

    replaceentries(var1, var2)
    
# Function that calculates unit conversion
def calcvar():
    global unit1
    global unit2
    global var1
    global var2
    global entry1
    global entry2
    
    var1 = float(entry1.get())
    print(var1)

    if gunit == "Temperature":
        x = var1
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

# IMPORTANT: THERE IS AN ISSUE WHEN CHANGING TEMPERATURE UNITS HERE
# Function to change first unit 
def callback1(selection):
    global unit1
    global gunit
    global uselection1
    uselection1 = selection
    xdict = typedict[gunit][0]
    unit1 = xdict[selection]
    calcvar()

# Function to change second unit
def callback2(selection):
    global unit2
    global gunit
    global uselection2
    uselection2 = selection
    xdict = typedict[gunit][0]
    unit2 = xdict[selection]
    calcvar()

# Get monitor dimensions
screen_width = pyautogui.size()[0]
screen_height = pyautogui.size()[1]

# Define the root window
root = Tk()
root.geometry("+" + str(int(0.1 * screen_width)) + "+" + str(int(0.2 * screen_height)))
root.resizable(False, False)
root.title("ConversionCalculator (v1.10.1)")
imagename = "icons8-weight-90.png"
image = PhotoImage(file = imagename)
root.iconphoto(False, image)
frm = ttk.Frame(root, padding=5)
frm2 = ttk.Frame(root, padding=5)

# Call grid method for frames
frm.grid()
frm2.grid()
    
# Define first unit for conversion
gunit = "Length"
var1 = 1.0
var2 = lengthdict["Meters (m)"] / lengthdict["Inches, International (in)"]
unit1 = 1
unit2 = 0.0254
uselection2 = "Inches, International (in)"
unitlist = lengthlist
unitlist = unitlist

# Set default selections for the options menus
default1 = StringVar(frm)
default1.set("Meters (m)")

default2 = StringVar(frm)
default2.set("Inches, International (in)")

default3 = StringVar(frm2)
default3.set("Length")

# Define first entry for number of units
entry1 = ttk.Entry(frm, width=24)
entry1.insert(END, var1)
entry1.grid(column=0, row=5, padx = 2)

# Define the first option menu for choosing conversion units
omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1)
omenu1.config(width=32)
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
omenu2.config(width=32)
omenu2.grid(column=4, row=5, padx = 2)

# Define the calculate button
calcbtt = ttk.Button(frm2, text="Calculate", command=calcvar)
calcbtt.grid(column=1, row=7, pady = 3)

# Define the option menu for selecting unit types
omenu3 = OptionMenu(frm2, default3, *typelist, command=changevar)
omenu3.grid(column=2, row=7, pady = 3)

# Mainloop
root.mainloop()
