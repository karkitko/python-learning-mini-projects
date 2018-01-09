print ("Celsius and Fahrenheit Converter")
inp = input("Would you like to know temperature in Celsius or Fahrenheit? C / F:")
if inp == "C":
    print ("What is the temperature in Fahrenheit?")
    temperature_Fahrenheit=float(input("Farenhait:"))
    Convert_F_na_C= 5/9 * (temperature_Fahrenheit - 32)
    print (Convert_F_na_C)

elif inp == "F":
    print ("What is the temperature in Celsius")
    temperature_Celsius=float(input("Celsius:"))
    Convert_C_na_F= 9/5 * (temperature_Celsius  + 32)
    print (Convert_C_na_F)
