
temp_fahrenheit = input("Enter Temperature in Fahrenheit:")
def convert(temp):
    temp_converted = 0.00
    temp_converted= (float(temp)-32)*5/9
    return temp_converted

print (convert(temp_fahrenheit))
