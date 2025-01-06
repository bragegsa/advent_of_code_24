import re
import numpy as np
from .day3_lib import import_data_day3

def format_data(data: str) -> list:
    '''
        Returns a formatted list where each element is separated by
        new lines
    '''

    data_formatted = np.array(data.split('\n'))

    return data_formatted

def xmas_search(data: list) -> int:
    ''' 
        Returns the number of times XMAS is written from left to right

        Args:
            data: a list of strings

        Returns:
            sum: number of times expressions are found
    '''

    # Use two regex expressions to find overlapping strings
    regex_xmas = 'XMAS'
    regex_samx = 'SAMX'
    sum = 0

    for row in data:

        sum += len(re.findall(regex_xmas, row))
        sum += len(re.findall(regex_samx, row))

    return sum

def get_diagonals(list_of_strings: list) -> list:
    '''
        Returns a list composed of all diagonal strings of
        the input list

        Args:
            list_of_strings: A list of strings

        Returns:
            diag_list: A list of strings
    '''

    matrix = [list(row[:]) for row in list_of_strings]
    m, n = np.shape(matrix)
    diag_list = []

    for i in range(-n, n):

        row = np.diagonal(matrix, i)
        diag_list.append(''.join(row))

    return diag_list


def rotate_list90(list_of_strings: list) -> list:
    '''
        Returns a list rotated by 90 degrees

        Args:
            list_of_strings: A list of strings

        Returns:
            list_rotated: input list rotated by 90 degrees
    '''

    matrix = [list(row[:]) for row in list_of_strings]
    m, n = np.shape(matrix)

    matrix_rotated = np.rot90(matrix)
    list_rotated = []

    for row in matrix_rotated:
        list_rotated.append(''.join(row))

    return list_rotated



def search_matrix(data: np.array) -> int:
    '''
        Returns the total number of times expression is found in 
        input data

        Args:
            data: A list of strings

        Returns:
            total: An int with the total number of times expression has been found
    '''

    total = 0

    total += xmas_search(data) # Search from left to right and vice versa
    total += xmas_search(get_diagonals(data)) # Search from top left to bottom right and vice versa

    data_rotated = rotate_list90(data)
    total += xmas_search(data_rotated) # Search from top to bottom and vice versa
    total += xmas_search(get_diagonals(data_rotated)) # Search from top right to bottom left and vice versa

    return total


def run_day4():
    '''
        This function solves the task for day 3
    '''

    print("\n--- Day 4 ---")

    data = import_data_day3(path='inputs/day4.txt')
    data_formatted = format_data(data)
    print(f'The number of times XMAS appears: {search_matrix(data_formatted)}')
   
if __name__ == "__main__":

    print("\n--- Running module directly ---")
    run_day4()