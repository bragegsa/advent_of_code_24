import pandas as pd
import re

def import_data_day3(path: str = 'inputs/day3.txt') -> str:
    '''
        Returns content of a txt file as a string
    '''

    f = open(path, "r")
    data = f.read()
    f.close()

    return data

def filter_data(data: list) -> list:
    '''
        Takes a string of data and finds all operations with
        respect to the criteria of the daily task
    '''

    list_of_operations = []
    regex = 'mul\([0-9]{1,3}\,[0-9]{1,3}\)'

    mul_operations = re.findall(regex, data)
    list_of_operations.extend(mul_operations)

    return list_of_operations

def compute_mul(operations: list) -> int:
    '''
        Computes the sum of the multiplication operations
    '''

    sum = 0
    regex = '[0-9]{1,3}'

    for operation in operations:

        product = 1
        numbers = re.findall(regex, operation)

        for number in numbers:

            product *= int(number)
         
        sum += product        

    return sum

def run_day3():
    '''
        This function solves the task for day 3
    '''

    print("\n--- Day 3 ---")

    data =import_data_day3()
    operations = filter_data(data)
    sum = compute_mul(operations)
    print(f'The sum of all Mul computations is: {sum}')
   
if __name__ == "__main__":

    print("\n--- Running module directly ---")
    run_day3()