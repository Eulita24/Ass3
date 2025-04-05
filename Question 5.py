# Sample list of Celsius temperatures
celsius_temperatures = [0, 20, 30, 40, 100]

# Using lambda and map to convert Celsius to Fahrenheit
fahrenheit_temperatures = list(map(lambda c: c * 9 / 5 + 32, celsius_temperatures))

# Print the converted list
print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)
