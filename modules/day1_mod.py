import pandas as pd

def import_data(path: str = 'inputs/day1.csv') -> pd.core.frame.DataFrame:
    '''
        Takes in the path of a csv file and returns a 
        dataframe of the given data. 
    '''

    data = pd.read_csv(path, header=None, names=['pair'])
    data[['List 1', 'List 2']] = data['pair'].str.split(expand=True).astype(int)
    data = data.drop(columns=['pair'])

    return data

def get_list(df: pd.core.frame.DataFrame, columnName: str) -> list:
    '''
        Takes in a dataframe and returns a list of the given
        column in the data frame
    '''

    list_unsorted = list(df[columnName])
    list_sorted = sorted(list_unsorted)

    return list_sorted

def get_distance_list(list1: list, list2: list) -> list:
    '''
        Takes in two lists and returns a list containing the absolute 
        distance between the corresponding elements in the lists
    '''

    distance_list = []

    for x, y in zip(list1, list2):
        distance_list.append(abs(x - y))

    return distance_list


def get_distance(distance_list: list) -> int:
    '''
        Takes in a list and returns the sum
    '''

    return sum(distance_list)