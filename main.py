#Python Tools ver 1.0
import tkinter as tk
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
    lenghsunit = ["1. Meter", "2. Kilometer", "3. Centimeter", "4. Millimeter", "5. Micrometer", "6. Nanometer", "7. Mile", "8. Yard", "9. Foot", "10. Inch"]
    funit = 0
    sunit = 0

    unit_value = { 
        "meter": 1000,
        "kilometer": 1000,
        "centimeter": 0.01,  
        "millimeter": 0.001,
        "micrometer": 0.000001,
    }
    print("WELCOME TO UNIT CONVERTER")
    print("Please select the type of conversion: ")
    for i in conversionlist:
        print(i)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Enter unit to convert from: ")

        for i in lenghsunit:
            print(i)
        funit = int(input(""))
        print(lenghsunit[funit-1])
        print("Enter unit to convert to: ")

        for i in lenghsunit:
            print(i)

        sunit = int(input(""))
        value = float(input("Enter value to convert: "))
        #Make the value into meters first(Base unit)
        value_in_meters = value * unit_value[lenghsunit[funit-1].strip('1234567890.').lower().strip()]
        #make a function so that it will only use scientific notation once the value_in_Meters varible reaches upto 8 digits/or when converting 0.9cm to meters.

        if(value_in_meters >= 0.000001):
            format_value = f"{value_in_meters:.7f}".rstrip("0")
        else:
            format_value = value_in_meters
            
        
        

        #After converting to meters, we then convert it to a desired unit.
        converted_value = value_in_meters / unit_value[lenghsunit[sunit-1].strip('1234567890.').lower().strip().rstrip("0")]
        
        print("\n" * 100)
        print(f"value from {lenghsunit[funit-1].strip('1234567890.').lower().strip()} to {lenghsunit[sunit-1].strip("01")}: {converted_value:.7f}")
        
        #print(f"Converting from {lenghsunit[funit-1].strip('12345678910.')} to {lenghsunit[sunit-1].strip('12345678910.')}") 



            

        #print(f"{lenghsunit[funit-1].strip('12345678910.')} = {kilometer} km")
        
        

while True:
    main_loop()