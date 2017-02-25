def celcius_to_fahrenheit(celcius):
    if (celcius < -273.15):
        return 0
    return celcius * 9/5 + 32

def temp_writer(temperatures):
    with(open("Temperatures.txt", "a")) as file:
        for temp in temperatures:
            if (temp > -273.15):
                temp = celcius_to_fahrenheit(temp)
                file.write(str(temp) + "\n")

temperatures = [10, -20, -289, 100]

temp_writer(temperatures)
