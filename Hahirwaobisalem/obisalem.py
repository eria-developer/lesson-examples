
def solve_puzzle():
  """
  Solving  a math puzzle involving exponentiation, division, and addition.

  Returns:
      tuple: A tuple containing the final value and its data type.
  """

  # --- Starting with Two Numbers ---
  base_number = 8  # Base number for the calculation
  exponent = 3     # Exponent value

  # --- Calculating the Power 
  power_result = base_number ** exponent  # Calculating  8 raised to the power of 3

  # --- Work with Another Number ---
  large_number = 50
  quotient = large_number // base_number  # Integer division (it ignores remainder)
  exact_division_result = large_number / base_number

  # --- Finding  the Final Value ---
  final_value = power_result + quotient + exact_division_result

  # --- Displaying  the final results ---
  # printing the ("Final Value:", final_value) 
  # printing the("Data Type:", type(final_value))

  return final_value, type(final_value)

if __name__ == "__main__":
  final_value, data_type = solve_puzzle()
  print("Final Value:", final_value)
  print("Data Type:", data_type)