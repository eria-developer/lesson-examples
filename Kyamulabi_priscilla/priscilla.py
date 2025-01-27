#python program to solve puzzle

base_number = 5
exponential_number = 8

power_result = base_number**exponential_number

print(power_result)

#Working with large number
large_number = 780

#quotient division
quotient_division =large_number//base_number
print (quotient_division)

#exact division
exact_division =large_number/base_number

print(exact_division)

#final value
final_value =power_result + quotient_division + exact_division

print(final_value)
print(type(final_value))