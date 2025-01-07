import re
import numpy as np

def format_data(data: str) -> list:
    '''
        Returns a formatted list where each element is separated by
        new lines
    '''

    data_formatted = np.array(data.split('\n'))

    return data_formatted

def xmas_search(data: list, regex_word: str = 'XMAS') -> int:
    ''' 
        Returns the number of times XMAS is written from left to right

        Args:
            data: a list of strings
            regex_word: word to search for

        Returns:
            sum: number of times expressions are found
    '''

    # Use two regex expressions to find overlapping strings
    regex_word_reverse = regex_word[::-1]
    sum = 0

    for row in data:

        sum += len(re.findall(regex_word, row))
        sum += len(re.findall(regex_word_reverse, row))

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

def matrix_search(data: list, regex_word: str = 'MAS') -> int:
    '''
        Returns the number of times a spesific word appears in an X-formation
        in a list of strings

        Args:
            data: list of strings
            regex_word: string to be found in X formation (Has to be odd)
        
        Returns:
            total: total number of times X formation appears
    '''

    matrix = [list(row[:]) for row in data]
    m,n = np.shape(matrix)
    total = 0
    padding = int(len(regex_word)/2)
    centre_letter = regex_word[int(len(regex_word)/2)]

    for i in range(padding, m-padding):

        for j in range(padding, n - padding):

            if(matrix[i][j] == centre_letter):

                window = [''.join(s[j-padding:j+padding+1]) for s in matrix[i-padding:i+padding+1]]
                window_rotated = rotate_list90(window)

                if (xmas_search(get_diagonals(window), regex_word) == 
                    xmas_search(get_diagonals(window_rotated), regex_word) and 
                    xmas_search(get_diagonals(window), regex_word) == 1):

                    total += 1


    return total


def run_day4():
    '''
        This function solves the task for day 3
    '''

    print("\n--- Day 4 ---")

    data = import_data_day3(path='inputs/day4.txt')
    data_formatted = format_data(data)
    print(f'The number of times XMAS appears: {search_matrix(data_formatted)}')
    print(f'The total number of X-MAS is: {matrix_search(data_formatted)}')
   
if __name__ == "__main__":

    from day3_lib import import_data_day3
    
    print("\n--- Running module directly ---")
    run_day4()

else:
    from .day3_lib import import_data_day3