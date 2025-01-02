import pandas as pd
from modules import get_list, get_distance, import_data, similarity_score

data = import_data()

list1 = get_list(data, 'List 1')
list2 = get_list(data, 'List 2')

print(f'Distance is: {get_distance(list1, list2)}')
print(f'Similarity score is: {similarity_score(list1, list2)}')