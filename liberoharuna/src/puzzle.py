#This is the very first python math programme by libero haruna.

base_number = 5
power_number = 2

result_number = base_number ** power_number

print(result_number)

#Introducing the third number.(the new one)
new_number = 102

#finding the approxiamte quotient.
roundoff_quotient = new_number//base_number
print(roundoff_quotient)

#finding the exact quotient.
exact_quotient = new_number/base_number
print(exact_quotient)

#Calculating the final value.
final_value = result_number + roundoff_quotient + exact_quotient
print(final_value)

#finding the value type of the final value 
print(type(final_value))