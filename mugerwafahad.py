# Step 1: Start with Two Numbers
base_number = 8  # Base of the calculation
exponent = 3  # Exponential power

# Step 2: Calculate the Power
power_result = base_number ** exponent  # 8^3

# Step 3: Work with Another Number
large_number = 50  # A number larger than base_number
quotient = large_number // base_number  # Whole number division (ignores remainder)
exact_division = large_number / base_number  # Exact division (includes decimals)

# Step 4: Find the Final Value
final_value = power_result + quotient + exact_division

# Step 5: Display the Results
print("Final Value:", final_value)
print("Type of Final Value:", type(final_value))

