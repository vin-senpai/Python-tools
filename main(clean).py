#Python Tools ver 1.0
import os
from games_clean import main
#Pure Cli(Without the design)

def main_loop():
    #Raw string
    #design = r"""",--------------------------===---.
| ACT-1B                          |
| ,----------------------------.  |         
| |  Welcome to python toolbox  | |
| |                             | |
| |                             | |         
| |  _.~"(_.~"(_.~"(_.~"(_.~"(  | |             
| |                             | |                ____        __  __                   __              __    
| |                             | |               / __ \__  __/ /_/ /_  ____  ____     / /_____  ____  / /____
| |                             | |              / /_/ / / / / __/ __ \/ __ \/ __ \   / __/ __ \/ __ \/ / ___/
| |                             | |             / ____/ /_/ / /_/ / / / /_/ / / / /  / /_/ /_/ / /_/ / (__  ) 
| |                             | |            /_/    \__, /\__/_/ /_/\____/_/ /_/   \__/\____/\____/_/____/  
| |                             | |                 /____/                                                     """

    
    
    print("Welcome to Python Tools ver 1.0")
    #print(design)
    print("Please select an option:    \n1. Games\n2. Unit converter\n3. Exit")
    
    choice = int(input(" "))
   
    
    if choice == 1:
        print("\n" * 200)
        main()
    elif choice == 2:
        print("\n" * 200)
        unit_converter()
    elif choice == 3:
        os._exit(0)
    else:
        print("Invalid option!")




def unit_converter():
    conversionlist = ["1. Length", "2. Weight"]
    lengthunitlist = ["1. Millimeter", "2. Centimeter", "3. Meter", "4. Kilometer", "5. Micrometer", "6. Nanometer", "7. Inches", "8. Foot", "9. Yards", "10. Miles"]
    weightunitlist = ["1. Microgram","2. Milligram","3. Gram","4. Kilogram","5. MetricTon"]
    funit = 0
    sunit = 0
    #This is a value we will use to convert any length unit into meter and also .
    standard_metric_unit = { 
        "millimeter": 1,
        "centimeter": 10,  
        "meter": 1000,
        "kilometer": 1000000,
        "micrometer": 0.001,
        "nanometer": 0.000001,
        "inches": 0.0393700787,
        "foot": 0.0032808399,
        "yards": 0.0010936133,
        "miles": 0.0000006213711922

    }

    imperial_metric_unit = {
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
    #Unit value for converting weights.
    standard_metric_weight_unit = {
        "microgram": 1,
        "milligram": 0.001,
        "gram": 0.000001,
        "kilogram":  0.000000001,
        "metricton": 0.000000000001

    }

    
    #print(r""" _____________________
#|  _________________  |
#| |              67.| |
#| |_________________| |
#|  ___ ___ ___   ___  |
#| | 7 | 8 | 9 | | + | |
#| |___|___|___| |___| |
#| | 4 | 5 | 6 | | - | |
#| |___|___|___| |___| |
#| | 1 | 2 | 3 | | x | |
#| |___|___|___| |___| |
#| | . | 0 | = | | / | |
#| |___|___|___| |___| |
#|_____________________|""")  

    print("WELCOME TO UNIT CONVERTER")
    print("Please select the type of conversion: ")
    for i in conversionlist: 
        print(i)

    choice = int(input('Enter your choice: '))

    #Length converter
    if choice == 1:
        print("Enter unit to convert from: ")

        for i in lengthunitlist:
            print(i)

        funit = int(input(""))
        print("Enter unit to convert to: ")

        for i in lengthunitlist:
            print(i)

        sunit = int(input(""))
        if(funit >= 11 or sunit >= 11):
            print("ERROR Wrong Value!")
            os._exit(0)
        value = float(input("Enter value to convert: "))

        #Convert the value into the smallest unit first(Base unit) and then convert it into desired unit.
        if(funit <= 6 and sunit <= 6): #Standard Metric system.
            value_in_mm = value * standard_metric_unit[lengthunitlist[funit-1].strip('1234567890.').lower().strip()]
            final_value = value_in_mm / standard_metric_unit[lengthunitlist[sunit-1].strip('1234567890.').lower().strip()]
            #print("i used metric")
        elif(funit >= 7 and sunit >= 7): #Imperial metric system.
            value_in_inches = value * imperial_metric_unit[lengthunitlist[funit-1].strip('123456789.').lower().strip()]
            final_value = value_in_inches / imperial_metric_unit[lengthunitlist[sunit-1].strip('1234567890.').lower().strip()]
            print(f"{lengthunitlist[funit-1].strip('1234567890.').lower().strip()} to inches is: {final_value}")
            #print("i used imperial")
        #Inorder to convert from imperial to metric(or vice versa),we must first con    vert them into their lowest value and convert both lowest value to desired unit.
        elif(funit <= 6 and sunit >= 7):
            value_in_mm = value * standard_metric_unit[lengthunitlist[funit-1].strip('1234567890.').lower().strip()]
            value_in_inches = value_in_mm * standard_metric_unit[lengthunitlist[sunit-1].strip('1234567890.').lower().strip()]
            final_value = value_in_inches   
            #print("std to imp")
        elif(funit >= 7 and sunit <= 6):
            value_in_inches = value * imperial_metric_unit[lengthunitlist[funit-1].strip('123456789.').lower().strip()]
            value_in_mm = value_in_inches *imperial_metric_unit[lengthunitlist[sunit-1].strip('123456789.').lower().strip()]
            final_value = value_in_mm
            #print("imp to std")
        else: 
            #final_value = value * standard_metric_unit[lengthunitlist[sunit-1].strip('1234567890.').lower().strip()]
            print("ERROR Invalid output!")
            #print("i used thiss")
        #make a function so that it will only use scientific notation once the value_in_mm varible reaches upto 8 digits/or when converting 0.9cm to meters.
        formatted_c_value =  f"{final_value:,.10f}".rstrip("0")

        # if(funit == 1 or sunit == 1):
        #     formatted_c_value =  f"{final_value:,.10f}".rstrip("0")
        #     print("i formatted it")
        # else:
        #     formatted_c_value =  f"{final_value:,.10f}".rstrip("0")
        #     print("i didn NOT formatted it")
           
      
        #Print final value.
        print(f"value from {lengthunitlist[funit-1].strip('1234567890.').lower().strip()}({value}) to {lengthunitlist[sunit-1].strip("01234567890.").lower().strip()}: {formatted_c_value}" )
        input("Press a Key to exit")
        print("\n" * 150)
        os.system("cls")
        #print(f"Converting from {lengthunitlist[funit-1].strip('12345678910.')} to {lengthunitlist[sunit-1].strip('12345678910.')}") 

        #print(f"{lengthunitlist[funit-1].strip('12345678910.')} = {kilometer} km")

    #Weigth convertre
    elif choice == 2:
        #Ask user for inputs
        print("Enter weigth to convert from: ")
        for i in weightunitlist:
            print(i)
        funit = int(input(" "))
        
        print("Enter weight unit to convert to: ")
        for i in weightunitlist:
            print(i)
        sunit = int(input(''))
        if(sunit >= 6 or funit >= 6):
            print("Error invalid option!")
            os._exit(0)
        w_value = float(input("Enter value to convert: "))

        #Just like from the length measurement, we convert the units to their lowest value
        value_in_micr = w_value / standard_metric_weight_unit[weightunitlist[funit-1].strip('1234567890.').lower().strip()]
        #Now we convert it to its desired value by multiplying
        weighted_converted = value_in_micr * standard_metric_weight_unit[weightunitlist[sunit-1].strip('1234567890.').lower().strip()]

        #Format its value so it wont use scientific notation.(Just keep it from now even it doest have a purpose yet.)
        formatted_w_value = weighted_converted
       
        print(f"value from{weightunitlist[funit-1].strip('1234567890.')}({w_value}) to {weightunitlist[sunit-1].strip('1234567890.')}: {round(formatted_w_value,9):,}")

    
        

    
while True:
    main_loop()
