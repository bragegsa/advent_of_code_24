import pandas as pd


def import_data(path: str = 'inputs/day1.csv') -> pd.core.frame.DataFrame:
    '''
        Takes in the path of a csv file and returns a
        dataframe of the given data.
    '''

    data = pd.read_csv(path, header=None, names=['pair'])
    data[['List 1', 'List 2']] = data['pair'].str.split(
        expand=True).astype(int)
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


def get_distance(list1: list, list2: list) -> int:
    '''
        Takes in two lists and returns the distance between them
    '''

    distance_list = []

    for x, y in zip(list1, list2):
        distance_list.append(abs(x - y))

    distance = sum(distance_list)

    return distance


def list_to_dictionary(list_to_transform: list) -> dict:

    dictionary = dict.fromkeys(set(list_to_transform), 0)

    for number in list_to_transform:

        dictionary[number] += 1

    return dictionary


def similarity_score(list1: list, list2: list) -> int:
    '''
        Takes list1 and determines a similarity score with list2
    '''

    score = 0

    list2_dict = list_to_dictionary(list2)

    for number in list1:

        if number in list2_dict:
            score += number * list2_dict[number]

    return score


def run_day1():
    '''
        This function solves the task for day 1
    '''

    print("\n--- Day 1 ---")

    data = import_data()

    list1 = get_list(data, 'List 1')
    list2 = get_list(data, 'List 2')

    print(f'Distance is: {get_distance(list1, list2)}')
    print(f'Similarity score is: {similarity_score(list1, list2)}')


if __name__ == "__main__":

    print("\n--- Running module directly ---")
    run_day1()
