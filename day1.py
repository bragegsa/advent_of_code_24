import pandas as pd
from modules import get_list, get_distance, get_distance_list, import_data

data = import_data()

list1 = get_list(data, 'List 1')
list2 = get_list(data, 'List 2')

distance = get_distance(get_distance_list(list1, list2))
print(distance)
