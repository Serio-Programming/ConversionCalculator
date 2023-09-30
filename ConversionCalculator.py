# ConversionCalculator
# Python 3.9.6
# A program by Tyler Serio
# This program converts units to other units

# Import
import tkinter
import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Define important unit dictionaries in terms of SI units
# https://en.wikipedia.org/wiki/List_of_conversion_factors
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

# Volume units dictionary
volumedict = {
    "Cubic Meters (m^3)": 1,
    "Cubic Miles (cu mi)": 4168181825.440579584,
    "Cubic Yards (yd^3)": 0.764554857984,
    "Cups, Metric (c)": 0.00025,
    "Liters (L)": 0.001,
    "Petroleum Barrels, Archaic Blue-Barrels": 0.158987294928
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

# Frequency units dictionary
freqdict = {
    "Actions per Minute (APM)": 1/60,
    "Cycles per Second (cps)": 1,
    "Degrees per Second (deg/s)": 0.00277777,
    "Hertz (Hz)": 1,
    "Radians per Second (rad/s)": 0.159155,
    "Revolutions per Minute (rpm)": 1/60
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
    #x = 10
    #print(eval(tempdict["Degrees Celsius(°C)"]))

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

# Define list of unit types
typelist = ["Length", "Volume", "Mass", "Time", "Frequency", "Temperature", "[Help Menu]"]

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
    
    if gunit == "[Help Menu]":
        return        

    elif gunit == "Length":
        unitlist = lengthlist
                
        default1.set("Meters (m)")
        unit1 = lengthdict["Meters (m)"]

        default2.set("Inches, International (in)")
        var2 = 1 / lengthdict["Inches, International (in)"]
        unit2 = lengthdict["Inches, International (in)"]

    elif gunit == "Volume":
        unitlist = volumelist
        
        default1.set("Cubic Meters (m^3)")
        unit1 = volumedict["Cubic Meters (m^3)"]

        default2.set("Cubic Yards (yd^3)")
        var2 = 1 / volumedict["Cubic Yards (yd^3)"]
        unit2 = volumedict["Cubic Yards (yd^3)"]
        
    elif gunit == "Mass":
        unitlist = masslist
        
        default1.set("Kilograms (kg)")
        unit1 = massdict["Kilograms (kg)"]

        default2.set("Pounds, Avoirdupois (lb av)")
        var2 = 1 / massdict["Pounds, Avoirdupois (lb av)"]
        unit2 = massdict["Pounds, Avoirdupois (lb av)"]

    elif gunit == "Time":
        unitlist = timelist

        default1.set("Seconds (s)")
        unit1 = timedict["Seconds (s)"]

        default2.set("Jiffies (j)")
        var2 = 1 / timedict["Jiffies (j)"]
        unit2 = timedict["Jiffies (j)"]

    elif gunit == "Frequency":
        unitlist = freqlist

        default1.set("Hertz (Hz)")
        unit1 = freqdict["Hertz (Hz)"]

        default2.set("Actions per Minute (APM)")
        var2 = 1 / freqdict["Actions per Minute (APM)"]
        unit2 = freqdict["Actions per Minute (APM)"]

    else:
        unitlist = templist

        default1.set("Kelvins (K)")
        unit1 = tempdict["Kelvins (K)"]

        default2.set("Degrees Celsius(°C)")
        x = 1
        var2 = eval(tempdict["Degrees Celsius(°C)"])
        unit2 = tempdict["Degrees Celsius(°C)"]

    var1 = 1.0        
    omenu1.destroy()
    omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1)
    omenu1.grid(column=1, row=5)
    omenu2.destroy()
    omenu2 = OptionMenu(frm, default2, *unitlist, command=callback2)
    omenu2.grid(column=4, row=5)

    entry1.destroy()
    entry1 = ttk.Entry(frm)
    entry1.insert(END, str(var1))    
    entry1.grid(column=0, row=5, padx = 2)

    entry2.destroy()
    entry2 = ttk.Entry(frm)
    entry2.insert(END, str(var2))
    entry2.grid(column=3, row=5, padx = 2)
    
    root.update()

def calcvar():
    global unit1
    global unit2
    global var1
    global var2
    global entry1
    global entry2
    
    var1 = float(entry1.get())

    if gunit == "Temperature":
        x = var1
        var2 = eval(unit2)
    else:
        var2 = (var1 * unit1) / unit2
        
    entry1.destroy()
    entry1 = ttk.Entry(frm)
    entry1.insert(END, str(var1))
    entry1.grid(column=0, row=5, padx = 2)

    entry2.destroy()
    entry2 = ttk.Entry(frm)
    entry2.insert(END, str(var2))
    entry2.grid(column=3, row=5, padx = 2)
    root.update()

def callback1(selection):
    global unit1
    global gunit
    global uselection1
    uselection1 = selection
    
    if gunit == "Length":
        unit1 = lengthdict[selection]
        
    elif gunit == "Volume":
        unit1 = volumedict[selection]
        
    elif gunit == "Mass":
        unit1 = massdict[selection]
        
    elif gunit == "Time":
        unit1 = timedict[selection]
        
    elif gunit == "Frequency":
        unit1 = freqdict[selection]
        
    else:
        unit1 = tempdict[selection]
        
    calcvar()

def callback2(selection):
    global unit2
    global gunit
    global uselection2
    uselection2 = selection
    if gunit == "Length":
        unit2 = lengthdict[selection]
    elif gunit == "Volume":
        unit2 = volumedict[selection]
    elif gunit == "Mass":
        unit2 = massdict[selection]
    elif gunit == "Time":
        unit2 = timedict[selection]
    elif gunit == "Frequency":
        unit2 = freqdict[selection]
    else:
        unit2 = tempdict[selection]
    calcvar()

def calculate():
    global entry1
    global entry2
    global unit1
    global unit2
    global var1
    global var2
    
    var1 = float(entry1.get())

    if gunit == "Temperature":
        x = var1
        var2 = eval(unit2)
    else:
        var2 = (var1 * unit1) / unit2
      
    entry1.destroy()
    entry1 = ttk.Entry(frm)
    entry1.insert(END, str(var1))
    entry1.grid(column=0, row=5, padx = 2)

    entry2.destroy()
    entry2 = ttk.Entry(frm)
    entry2.insert(END, str(var2))
    entry2.grid(column=3, row=5, padx = 2)
    
    root.update()

# Get monitor dimensions
screen_width = pyautogui.size()[0]
screen_height = pyautogui.size()[1]

# Define the root window
root = Tk()
root.geometry("+" + str(int(0.1 * screen_width)) + "+" + str(int(0.2 * screen_height)))
root.resizable(False, False)
root.title("ConversionCalculator")
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

# Define the entry forms, buttons, and menus
entry1 = ttk.Entry(frm)
entry1.insert(END, var1)
entry1.grid(column=0, row=5, padx = 2)

omenu1 = OptionMenu(frm, default1, *unitlist, command=callback1) # trace the variable
omenu1.grid(column=1, row=5, padx = 2)

islabel = ttk.Label(frm, text=f"is equal to ")
islabel.grid(column=2, row=5, padx = 2)

entry2 = ttk.Entry(frm)
entry2.insert(END, str(var2))
entry2.grid(column=3, row=5, padx = 2)

omenu2 = OptionMenu(frm, default2, *unitlist, command=callback2) # trace the variable
omenu2.grid(column=4, row=5, padx = 2)

calcbtt = ttk.Button(frm2, text="Calculate", command=calculate)
calcbtt.grid(column=1, row=7, pady = 3)

omenu3 = OptionMenu(frm2, default3, *typelist, command=changevar)
omenu3.grid(column=2, row=7, pady = 3)

root.mainloop()
