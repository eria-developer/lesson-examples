# Python program to solve the puzzle

base_number = 2
exponential_number =5

power_result =base_number**exponential_number

print (power_result)

#working with large number
large_number = 80

# Quotient division
quotient_division = large_number//base_number

print(quotient_division)

#Exact division
exact_division = large_number/base_number

print(exact_division)

#Final value 
final_value = power_result + quotient_division + exact_division

print(final_value)

print(type(final_value))