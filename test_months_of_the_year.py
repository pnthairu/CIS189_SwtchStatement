# Start Program
"""
Program: test_months_of_the_year.py
Author: Paul Thairu
Last date modified: 06/23/2020

declare an unimplemented function in_set.
This will eventually accept a set and return a boolean value stating if the element is in the set.
First, it contains pass only.
"""
from switch_statement import months_of_the_year

tests_switch = (months_of_the_year.switch_score(1) == 'January',
         months_of_the_year.switch_score(2) == 'February',
         months_of_the_year.switch_score(13) == 'April')
for i in tests_switch:
    print("Pass" if i else "Fail")


