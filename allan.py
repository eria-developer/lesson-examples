base_number = 7 # Base of the calculation
exponent = 3     # Number of times the base is multiplied by itself

# Step 2: Calculate the Power
power_result = base_number ** exponent  # Exponential calculation

# Step 3: Work with Another Number
larger_number = 50  # A third number larger than the base number
quotient = larger_number // base_number  # Integer division (quotient)
exact_division_result = larger_number / base_number  # Exact division (floating-point)

# Step 4: Find the Final Value
final_value = power_result + quotient + exact_division_result

# Step 5: Display the Results
print("Final Value:", final_value)
print("Type of Final Value:", type(final_value))