# Start Program
"""
Program: months_of_the_year.py
Author: Paul Thairu
Last date modified: 06/23/2020

Program that uses switch to convert months of the year to numbers that represents the months
eg 1 will represent january etc

"""

# KeyA function for the month of January
def KeyA():

    return 'January'

# KeyB function for the month of February
def KeyB():

    return 'February'

# KeyC function for the month of March
def KeyC():

    return 'March'

# KeyD function for the month of April
def KeyD():

    return 'April'

# KeyE function for the month of May
def KeyE():
    return 'May'

# KeyF function for the month of June
def KeyF():
    return 'June'

# KeyG function for the month of July
def KeyG():
    return 'July'

# KeyH function for the month of August
def KeyH():
    return 'August'

# KeyI function for the month of September
def KeyI():
    return 'September'

# KeyJ function for the month of October
def KeyJ():
    return 'October'

# KeyK function for the month of November
def KeyK():
    return 'November'

# KeyA function for the month of December
def KeyL():
    return 'December'

# Default function
def noKey():
    return "Invalid number to represent the month (1-12)"

# Function to cover month to number using switch
def switch_score(key):
    switch = {
      1: KeyA(),  # January is 1
      2: KeyB(),  # February is 2
      3: KeyC(),  # March is 3
      4: KeyD(),  # April is 4
      5: KeyE(),  # May is 5
      6: KeyF(),  # June is 6
      7: KeyG(),  # July is 7
      8: KeyH(),  # August is 8
      9: KeyI(),  # September is 9
      10: KeyJ(),  # October is 10
      11: KeyK(),  # November is 11
      12: KeyL()  # December is 12
    }
    # variable month that is converted to switch
    month = switch.get(key, noKey())

    return month


if __name__ == '__main__':

    month_num = int(input("Please enter number that represents the month: "))

    print(month_num, "=", switch_score(month_num))  # call switch_score function

# End program
