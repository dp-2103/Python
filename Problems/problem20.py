# Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
print(f"{f_to_c(f)} °C")

#round off value
print(f"{round(f_to_c(f))} °C")

#round off till 2 decimals    round(func, decimals)
print(f"{round(f_to_c(f), 2)} °C")