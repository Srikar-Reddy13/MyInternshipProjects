def converter(value, unit1, unit2):  # This function converts units based on provided values
    
    if unit1 == "m" and unit2 == "cm":
        return value * 100  # Converts meters to centimeters
    elif unit1 == "cm" and unit2 == "m":
        return value / 100  # Converts centimeters to meters
    elif unit1 == "m" and unit2 == "mm":
        return value * 1000  # Converts meters to millimeters
    elif unit1 == "mm" and unit2 == "m":
        return value / 1000  # Converts millimeters to meters
    elif unit1 == "cm" and unit2 == "mm":
        return value * 10  # Converts centimeters to millimeters
    elif unit1 == "mm" and unit2 == "cm":
        return value / 10  # Converts millimeters to centimeters
    elif unit1 == "m" and unit2 == "km":
        return value / 1000  # Converts meters to kilometers
    elif unit1 == "km" and unit2 == "m":
        return value * 1000  # Converts kilometers to meters
    elif unit1 == "m" and unit2 == "ft":
        return value * 3.28084  # Converts meters to feet
    elif unit1 == "ft" and unit2 == "m":
        return value / 3.28084  # Converts feet to meters
    elif unit1 == "ft" and unit2 == "in":
        return value * 12  # Converts feet to inches
    elif unit1 == "in" and unit2 == "ft":
        return value / 12  # Converts inches to feet
    elif unit1 == "c" and unit2 == "f":  
        return (value * 9/5) + 32  # Converts Celsius to Fahrenheit
    elif unit1 == "f" and unit2 == "c": 
        return (value - 32) * 5/9  # Converts Fahrenheit to Celsius
    else:
        return "Conversion not supported"  # Returns if the conversion condition is not supported

value = float(input("Enter value: ")) # Taking input value from the user
unit1_inp = input("From unit (m, cm, mm, km, ft, in, c, f): ").lower() #Taking input of unit1 parameter
unit2_inp = input("To unit (m, cm, mm, km, ft, in, c, f): ").lower() #Taking input of unit2 parameter

result = converter(value, unit1_inp, unit2_inp)
print(f"Result: {value} {unit1_inp} is equal to {result} {unit2_inp}")  # Displays the final result

