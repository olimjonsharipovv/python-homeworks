def convertion_to_far(celsius):
     return celsius * 9 / 5 + 32

def convertion_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit_input = float(input("Enter a temperature in Fahrenheit: "))
celsius_output = convertion_to_cel(fahrenheit_input)
print(f"{fahrenheit_input} degrees F = {round(celsius_output, 2)} degrees C")

celsius_input = float(input("Enter a temperature in Celsius: "))
fahrenheit_output = convertion_to_far(celsius_input)

print(f"{celsius_input} degrees C = {round(fahrenheit_output, 2)} degrees F")












