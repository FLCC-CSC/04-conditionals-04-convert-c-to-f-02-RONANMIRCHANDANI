# FILE NAME - convert_C_to_F_02.py

# NAME: Ronan Mirchandani
# DATE: 10/2/25
# BRIEF DESCRIPTION: Temprature Converter.  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("=====Temprature Converter=====")
print()
print("  1. Convert from Celsius to Fahrenheit ")
print("  2. Convert from Fahrenheit to Celsius")
print()
FFF = int(input(f'Please choose from the above menu: '))

if FFF == 1: 
  cc = int(input(f'Enter a temperture to convert: '))
  jack = (cc * 9/5) + 32
  print()
  print(f'{cc} degrees Celsius is {jack} Fahrenheit.')
if FFF == 2:
  cc2 = int(input('Enter a temperture to convert: '))
  anna = (cc2 - 32) * 5/9
  print()
  print(f'{cc2} degrees Farenheit is {anna} celsius.')


    






########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?


if statements have a very particular organization that cannot be miss-matched. It will ruin your code. 




'''
