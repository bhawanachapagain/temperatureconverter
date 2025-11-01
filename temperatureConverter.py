# Temperature Converter Program
# Converts between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

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


def main():
    print("🌡️ Temperature Converter")
    print("Available units: Celsius (C), Fahrenheit (F), Kelvin (K)")

    try:
        temp = float(input("Enter the temperature value: "))
        from_unit = input("Convert from (C/F/K): ").strip().upper()
        to_unit = input("Convert to (C/F/K): ").strip().upper()

        if from_unit == to_unit:
            print(f"No conversion needed. Result: {temp:.2f}°{to_unit}")
            return

        # Conversion logic
        if from_unit == "C":
            result = celsius_to_fahrenheit(temp) if to_unit == "F" else celsius_to_kelvin(temp)
        elif from_unit == "F":
            result = fahrenheit_to_celsius(temp) if to_unit == "C" else fahrenheit_to_kelvin(temp)
        elif from_unit == "K":
            result = kelvin_to_celsius(temp) if to_unit == "C" else kelvin_to_fahrenheit(temp)
        else:
            print("❌ Invalid input unit. Please choose C, F, or K.")
            return

        print(f"✅ Converted temperature: {result:.2f}°{to_unit}")

    except ValueError:
        print("⚠️ Please enter a valid numerical temperature.")


if __name__ == "__main__":
    main()
