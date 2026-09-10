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
    lenghsunit = ["1. Millimeter", "2. Centimeter", "3. Meter", "4. Kilometer", "5. Micrometer", "6. Nanometer", "7. Mile", "8. Yard", "9. Foot", "10. Inch"]
    funit = 0
    sunit = 0
    #This is a value we will use to convert any unit into meter.

    meter_unit_value = { 
        "meter": 1000,
        "kilometer": 1000000,
        "centimeter": 10,  
        "millimeter": 1,
        "micrometer": 0.000001,
        "nanometer": 0.000000001,
    }

    converting_meter_unit_value = {
        "meters": 1,
        "kilometer": 1000,
        "centimeter": 10000,
    }
    print("WELCOME TO UNIT CONVERTER")
    print("Please select the type of conversion: ")
    
    for i in conversionlist:
        print(i)

    choice = int(input('Enter your choice: '))

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

        #Convert the value into the smallest unit first(Base unit)
        value_in_mm = value * meter_unit_value[lenghsunit[funit-1].strip('1234567890.').lower().strip()]
         #After converting to meters, we then convert it to a desired unit.
        if(not funit == 1):
            converted_value = value_in_mm / meter_unit_value[lenghsunit[sunit-1].strip('1234567890.').lower().strip()]    
        else:
            converted_value = value * meter_unit_value[lenghsunit[sunit-1].strip('1234567890.').lower().strip()] #no need for value in meters if value given is already in meter
        #make a function so that it will only use scientific notation once the value_in_mm varible reaches upto 8 digits/or when converting 0.9cm to meters.

        if(value_in_mm > 0.000001):
            formatted_m_value = f"{value_in_mm:.7f}".rstrip("0")
        else:
            formatted_m_value = value_in_mm 

       

        if(converted_value > 0.000001):
            formatted_c_value = f"{converted_value:.7f}".strip('.').rstrip("0")
            print("yes it is")
        elif(sunit == 0):
            formatted_c_value = value_in_mm
        else:
            formatted_c_value = converted_value
            print("i used this value really")


        print("\n" * 100)
        print(f"Value in millimeters: {value_in_mm}")
        print(f"value from {lenghsunit[funit-1].strip('1234567890.').lower().strip()}({value}) to {lenghsunit[sunit-1].strip("01234567890.").lower().strip()}: {formatted_c_value}" )
        
        #print(f"Converting from {lenghsunit[funit-1].strip('12345678910.')} to {lenghsunit[sunit-1].strip('12345678910.')}") 



            

        #print(f"{lenghsunit[funit-1].strip('12345678910.')} = {kilometer} km")
        
        

while True:
    main_loop()