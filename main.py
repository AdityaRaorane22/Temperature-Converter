def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == "__main__":
    temp = float(input("Enter temperature: "))
    scale = input("Enter scale (C/F/K): ").upper()
    if scale == "C":
        print(f"{temp}C = {celsius_to_fahrenheit(temp)}F = {celsius_to_kelvin(temp)}K")
    elif scale == "F":
        print(f"{temp}F = {fahrenheit_to_celsius(temp)}C")
    elif scale == "K":
        print(f"{temp}K = {kelvin_to_celsius(temp)}C")
    else:
        print("Invalid scale")
