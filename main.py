#Python Tools ver 1.0
import tkinter as tk
import os
from tkinter import ttk 


def main_loop():
    print("Welcome to Python Tools ver 1.0")
    # choice = int(input("Please select an option:\n1. Image viewer\n2. Unit converter\n3. Exit\n4."))

    # if choice == 1:
    #     image_viewer()
    # elif choice == 2:
    #     unit_converter()
    unit_converter()


def image_viewer():
    root = tk.Tk()
    root.title("Image Viewer")
    tk.Frame(root, width=400, height=500).pack()
    root.mainloop()

def unit_converter():
    conversionlist = ["1. Length", "2. Weight", "3. Temperature"]
    unitlist = ["1. Millimeter", "2. Centimeter", "3. Meter", "4. Kilometer", "5. Micrometer", "6. Nanometer", "7. Inches", "8. Foot", "9. Yards", "10. Miles"]
    funit = 0
    sunit = 0
    #This is a value we will use to convert any unit into meter.

    standard_metric_unit = { 
        "meter": 1000,
        "kilometer": 1000000,
        "centimeter": 10,  
        "millimeter": 1,
        "micrometer": 0.000001,
        "nanometer": 0.000000001,

        "inches": 0.0393700787,
        "foot": 0.0032808399,
        "yards": 0.0010936133,
        "miles": 6.213711922E-7

    }

    imperial_metri_unit = {
        "inches": 1,
        "foot": 12,
        "yards": 36,
        "miles": 63360, 

        "millimeter": 25.4,
        "centimeter": 2.54,
        "meter": 0.0254,
        "kilometer": 0.0000254,
        "micrometer": 25400,
        "nanometer": 25400000

    }

    print("WELCOME TO UNIT CONVERTER")
    print("Please select the type of conversion: ")
    
    for i in conversionlist:
        print(i)

    choice = int(input('Enter your choice: '))

    if choice == 1:
        print("Enter unit to convert from: ")

        for i in unitlist:
            print(i)
        funit = int(input(""))
        print(unitlist[funit-1])
        print("Enter unit to convert to: ")

        for i in unitlist:
            print(i)

        sunit = int(input(""))
        value = float(input("Enter value to convert: "))

        #Convert the value into the smallest unit first(Base unit) and then convert it into desired unit.
        if(funit <= 5 and sunit <= 5): #Standard Metric system.
            value_in_mm = value * standard_metric_unit[unitlist[funit-1].strip('1234567890.').lower().strip()]
            final_value = value_in_mm 
        elif(funit > 5 and sunit > 5): #Imperial metric system.
            value_in_inches = value * imperial_metri_unit[unitlist[funit-1].strip('123456789.').lower().strip()]
            final_value = value_in_inches
            print(f"{unitlist[funit-1].strip('1234567890.').lower().strip()} to inches is: {final_value}")
            print(f"Inches to yards is: {value_in_inches / 36}")
        #Inorder to convert from imperial to metric(or vice versa),we must first convert them into their lowest value and convert both lowest value to desired unit.
        elif(funit <= 5 and sunit >= 6):
            value_in_mm = value * standard_metric_unit[unitlist[funit-1].strip('1234567890.').lower().strip()]
            value_in_inches = value_in_mm * standard_metric_unit[unitlist[sunit-1].strip('1234567890.').lower().strip()]
            final_value = value_in_inches   
        elif(funit >= 6 and sunit <= 5):
            value_in_inches = value * imperial_metri_unit[unitlist[funit-1].strip('123456789.').lower().strip()]
            value_in_mm = value_in_inches * imperial_metri_unit[unitlist[sunit-1].strip('123456789.').lower().strip()]
            final_value = value_in_mm
        else:
            print("ERROR wrong")
           
        
        
        #make a function so that it will only use scientific notation once the value_in_mm varible reaches upto 8 digits/or when converting 0.9cm to meters.

        if(final_value > 0.000001):
            formatted_m_value = f"{final_value:.7f}".rstrip("0")
        else:
            formatted_m_value = final_value

        if(final_value > 0.000001):
            formatted_c_value = f"{final_value:.7f}".strip('.').rstrip("0")
            print("yes it is")
        elif(sunit == 0):
            formatted_c_value = value_in_mm
        else:
            formatted_c_value = final_value
            print("i used this value really")


        os.system("cls")
        print(f"value from {unitlist[funit-1].strip('1234567890.').lower().strip()}({value}) to {unitlist[sunit-1].strip("01234567890.").lower().strip()}: {formatted_c_value}" )
        input("Press a Key to exit")
        os.system("cls")
        #print(f"Converting from {unitlist[funit-1].strip('12345678910.')} to {unitlist[sunit-1].strip('12345678910.')}") 

        #print(f"{unitlist[funit-1].strip('12345678910.')} = {kilometer} km")
        
        

while True:
    main_loop()