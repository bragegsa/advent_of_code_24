import pandas as pd
import re


def import_data_day3(path: str = 'inputs/day3.txt') -> str:
    '''
        Returns content of a txt file as a string

        Args:
            path: the path to input file

        Returns:
            data: A string of data from input file
    '''

    f = open(path, "r")
    data = f.read()
    f.close()

    return data


def filter_data(data: list, extra_instructions: bool = False) -> list:
    '''
        Takes a string of data and finds all operations with
        respect to the criteria of the daily task

        Args:
            data: A string of data
            extra_instructions: Enabels the use of more than the mul operation

        Returns:
            list_of_operations: A list of operations
    '''

    list_of_operations = []

    if extra_instructions:
        regex = 'mul\\([0-9]{1,3}\\,[0-9]{1,3}\\)|do\\(\\)|don\'t\\(\\)'
    else:
        regex = 'mul\\([0-9]{1,3}\\,[0-9]{1,3}\\)'

    mul_operations = re.findall(regex, data)
    list_of_operations.extend(mul_operations)

    return list_of_operations


def compute_mul(operations: list) -> int:
    '''
        Computes the sum of the multiplication operations

        Args:
            operations: A list of operations to be performed

        Returns:
            sum: The sum of all operations
    '''

    sum = 0
    regex = '[0-9]{1,3}'
    skip = False

    for operation in operations:

        product = 1
        numbers = re.findall(regex, operation)

        if operation == 'do()':

            skip = False

        elif operation == 'don\'t()':

            skip = True

        elif not skip:

            for number in numbers:

                product *= int(number)

            sum += product

    return sum


def run_day3():
    '''
        This function solves the task for day 3
    '''

    print("\n--- Day 3 ---")

    data = import_data_day3()
    operations = filter_data(data)
    sum = compute_mul(operations)
    print(f'The sum of all Mul computations is: {sum}')

    operations_part2 = filter_data(data, extra_instructions=True)
    sum_part2 = compute_mul(operations_part2)
    print(f'The sum of all Mul computations is: {sum_part2}')


if __name__ == "__main__":

    print("\n--- Running module directly ---")
    run_day3()
