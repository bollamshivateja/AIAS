# Python program to calculate electricity (power) bill

# Step 1: Get user inputs
house_number = input("Enter your house number: ")
purpose = input("Enter the purpose (Domestic/Industrial): ").strip().lower()
previous_units = float(input("Enter previous meter reading (units): "))
present_units = float(input("Enter present meter reading (units): "))

# Step 2: Calculate units consumed
units_consumed = present_units - previous_units
print(f"\nHouse Number: {house_number}")
print(f"Purpose: {purpose.capitalize()}")
print(f"Previous Units: {previous_units}")
print(f"Present Units: {present_units}")
print(f"Units Consumed: {units_consumed}")

# Step 3: Set rate per unit based on purpose
if purpose == "domestic":
    rate = 5.0  # Example rate for domestic
elif purpose == "industrial":
    rate = 8.0  # Example rate for industrial
else:
    print("Invalid purpose entered. Please enter either 'Domestic' or 'Industrial'.")
    exit(1)

print(f"Rate per unit: Rs. {rate}")

# Step 4: Calculate total bill
bill_amount = units_consumed * rate
print(f"Total Bill Amount: Rs. {bill_amount:.2f}")
