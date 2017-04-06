
is_temp = input("Temperature is F for Fahrenheit or C for Celcius:")

def convert(temp):
    temp_converted = 0.00
    if temp.lower() == "f":
        temp_fahrenheit = input("Enter Temperature in Fahrenheit:")
        temp_converted= "Celcius:"+str((float(temp_fahrenheit)-32)*5/9)
    elif temp.lower() == "c":
        temp_celcius = input("Enter Temperature in Celcius:")
        temp_converted= "Fahrenheit:" + str((float(temp_celcius)*9/5)+32)
    return temp_converted

print (convert(is_temp))
