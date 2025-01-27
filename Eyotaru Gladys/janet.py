#solve puzzle

base_number= 9
exponential_number=6
power_result=base_number**exponential_number

print(power_result)

#working with large numbers
large_number=120

quotient_division=large_number//base_number 
print(quotient_division)

#actual division
actual_division= large_number/base_number

print(actual_division)


#total value
total_value= power_result +quotient_division+ actual_division
print(total_value)
print(type(total_value))