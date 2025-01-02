import pandas as pd

def import_data_day2(path: str = 'inputs/day2.csv') -> list:
    '''
        Takes in the path of a csv file and returns a 
        2D list of the given data. 
    '''

    data = pd.read_csv(path, header=None)
    data_list = []

    for element in data[0]:
        new_row = list(map(int, element.split()))
        data_list.append(new_row)

    return data_list


def check_if_list_safe(list_to_check: list) -> bool:
    '''
        Takes a list and checks if the report is safe based
        on criteria from Task (Day 2)
    '''

    is_increasing_start = bool
    is_increasing = bool

    for i in range(1, len(list_to_check)):

        difference = list_to_check[i] - list_to_check[i - 1]
        abs_difference = abs(difference)
        is_increasing = bool(difference > 0)

        if (i == 1):
            
            is_increasing_start = is_increasing 
        

        if (abs_difference < 1 or 3 < abs_difference or is_increasing_start != is_increasing):

            return False


    return True

def number_of_safe_reports(matrix_to_check: list) -> int:
    '''
        Takes a two dimensional list and checks each list (report)
        if it is safe and counts the number of safe lists
    '''

    number_of_safe_reports = 0

    for row in matrix_to_check:

        if check_if_list_safe(row):

            number_of_safe_reports += 1

    return number_of_safe_reports

