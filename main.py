'''
Find PI to the Nth Digit

Enter a number and have the program generate pi up to that many decimal places.
Keep a limit to how far the program will go.

Challange problem from Jose Portilla
Project from Final Capstone Project Ideas - 
https://www.udemy.com/course/complete-python-bootcamp/


Created 6/8/2022
CodingWithDude.com
Ryan Austin
CodingWithDude@gmail.com
'''

from decimal import *
import math

my_pi = Decimal(math.pi) # using Decimal to get an extened float decimal length of 28

def format_pi():
    print('Welcome to Find π to the Nth Digit!')
    print('This program will return a specific number of digits of π between 0 and 28 inclusive.')
    while True:
        try:
            n = int(input('Please enter how many decimal places of pi you want returned: '))
            if n >= 0 and n <= 28:
                break
            else:
                print('That is not a valid choice')
                continue
        except:
            print('That is not a valid choice')   

    n_str = str(n) # setting n to a string to be concatenated within the {:.2f}.format method where 2 is the decimal length
    format_condition = '{:.' + n_str + 'f}' # reads {:.'n_str'f} ie n_str = 2 is {:.2f}

    formatted_pi = format_condition.format(my_pi) # using the concatenated string created for the {:.2f}.format method
    print(formatted_pi)

if __name__ == '__main__':
    while True:
        format_pi()
        run_again = input('Would you like to play again? (y/n)? ')
        if run_again.lower().startswith('y'):
            continue
        else:
            print('Thanks for using Find π to the Nth Digit!')
        break
