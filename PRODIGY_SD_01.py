def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Conversion Program")
    print("Please select the current temperature unit:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {fahrenheit}°F")
            print(f"{celsius}°C = {kelvin}K")
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")
    
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {celsius}°C")
            print(f"{fahrenheit}°F = {kelvin}K")
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")
    
    elif choice == '3':
        try:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K = {celsius}°C")
            print(f"{kelvin}K = {fahrenheit}°F")
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
