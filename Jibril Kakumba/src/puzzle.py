#Python program that solves a math puzzle

#Puzzle base
base_number = 3
expotential_number = 8

#Result
expotential_result = base_number ** expotential_number

print(expotential_result)

#Large number
third_number = 70

#Quotient result
quotient_division = third_number//base_number

print(quotient_division)

#Exact result
exact_division = third_number/base_number

print(exact_division)

#Final Value
final_value = expotential_result + quotient_division + exact_division

print(final_value)

#Finding value type
print(type(final_value))