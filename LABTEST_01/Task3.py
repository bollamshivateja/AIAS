def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def parse_input(user_input):
    user_input = user_input.strip().lower()
    # Example: "20 c", "30 f", "273.15 k"
    parts = user_input.split()
    if len(parts) != 2:
        return None, None
    try:
        value = float(parts[0])
    except ValueError:
        return None, None
    unit = parts[1]
    if unit not in ['c', 'f', 'k']:
        return None, None
    return value, unit

if __name__ == "__main__":
    print("Temperature Converter")
    print("Enter temperature with unit (e.g., 20 c, 68 f, 300 k)")
    user_input = input("Enter temperature: ")
    value, unit = parse_input(user_input)
    if value is None or unit is None:
        print("Invalid input format.")
    else:
        if unit == 'c':
            f = celsius_to_fahrenheit(value)
            k = celsius_to_kelvin(value)
            print(f"{value} C = {f:.2f} F, {k:.2f} K")
        elif unit == 'f':
            c = fahrenheit_to_celsius(value)
            k = fahrenheit_to_kelvin(value)
            print(f"{value} F = {c:.2f} C, {k:.2f} K")
        elif unit == 'k':
            c = kelvin_to_celsius(value)
            f = kelvin_to_fahrenheit(value)
            print(f"{value} K = {c:.2f} C, {f:.2f} F")
