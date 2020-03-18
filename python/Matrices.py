# Matrices.py
# Author: Taylor Marrion
# Date: 2/9/2020
"""This application allows a user to enter the values of two, 3x3 matrices and then select from options including, addition, subtraction, matrix multiplication, and element by element multiplication."""

import numpy as np

def get_selection():
    """prompts user for selection or to quit"""
    while True: # int type input validation
        try:
            print ('Select from the following menu:')
            print ('1. Addition')
            print ('2. Subtraction')
            print ('3. Matrix Multiplication')
            print ('4. Element by element multiplication')
            print ('5. Exit the Application')
            selection = int(input('Enter your selection: '))
            return (selection)
        except ValueError:
            print ('Invalid option! Please enter an Integer between 1-5!')
# end get_selection

def get_matrix():
    """Prompts user for integers to populate 3x3 matrix"""
    numbers = []
    size = 9
    for i in range(size):
        while len(numbers) < 9:
            try:
                temp = int(input('Enter an integer: '))
                numbers.append(temp)
            except ValueError:
                print ('Invalid entry!')
    numbers = np.array(numbers)
    numbers.resize(3,3)
    return numbers
# end get_matrix

def generate_output(selection):
    """Generates output based on user selection."""
    numbers1 = get_matrix()
    print ('Your first 3x3 matrix is:')
    print (numbers1)
    numbers2 = get_matrix()
    print ('Your second 3x3 matrix is:')
    print (numbers2)
    numbers3 = []
    
    if selection == 1:
        print ('You chose Addition. The results are:')
        numbers3 = np.add(numbers1, numbers2)
    elif selection == 2:
        print ('You chose Subtraction. The results are:')
        numbers3 = np.subtract(numbers1, numbers2)
    elif selection == 3:
        print ('You chose Matrix Multiplication. The results are:')
        numbers3 = np.dot(numbers1, numbers2)
    elif selection == 4:
        print ('You chose Element by element multiplication. The results are:')
        numbers3 = np.multiply(numbers1, numbers2)
    else: # range check input validation
        print ('Invalid option! Please enter an Integer between 1-5!')
    # end if-elif-else block
    print (numbers3)
    print ('The Transpose is:')
    print (numbers3.T)
    print ('The row and column mean values of the results are:')
    rows = np.array2string(numbers3.mean(axis=1))
    print (f'Row: {rows}')
    columns = np.array2string(numbers3.mean(axis=0))
    print (f'Column: {columns}')
# end generate_output

# start main body of code
# print welcome message
print ('***************** Welcome to the Python Matrix Application***********')

# prompt user for selection with sentinel-controlled iteration

selection = get_selection()
exit_int = 5
while selection != exit_int:
    generate_output(selection)
    selection = get_selection()
# end while loop
print ('You selected %d to quit.' % exit_int)

# print goodbye message
print ('*************** Thanks for playing the Matrix Game **********')