def celcius_to_fahrenheit(celcius):
    if (celcius < -273.15):
        return "That temperature doesn't make sense"
    return celcius * 9/5 + 32

temperatures = [10, -20, -289, 100]

for temp in temperatures:
    temp = celcius_to_fahrenheit(temp)
    print(temp)
