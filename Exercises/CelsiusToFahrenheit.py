def celcius_to_fahrenheit(celcius):
    if (celcius < -273.15):
        print("Celcius temperature too low")
        return
    return celcius * 9/5 + 32

temp = celcius_to_fahrenheit(-300)
print(temp)
