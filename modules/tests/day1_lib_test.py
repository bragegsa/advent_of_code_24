import pandas as pd
import modules.day1_lib as mod

# --- Test data: ---
df_test = pd.DataFrame({
        "List 1": [3, 4, 2, 1, 3, 3],
        "List 2": [4, 3, 5, 3, 9, 3]
    })

list1_test = [1, 2, 3, 3, 3, 4]
list2_test = [3, 3, 3, 4, 5, 9]

# --- Test Functions: ---
def test_import_data():
    
    df_imported = mod.import_data('inputs/inputs_test/day1_test.csv')
    pd.testing.assert_frame_equal(df_imported, df_test)

def test_get_list():

    list1_test = [1, 2, 3, 3, 3, 4]
    list1_sorted = mod.get_list(df_test, 'List 1')
    assert list1_sorted == list1_test

def test_get_distance():

    
    distance = mod.get_distance(list1_test, list2_test)
    
    assert distance == 11

def test_list_to_dictionary():

    list_dict_test = {1: 1, 2: 1, 3: 3, 4: 1}

    list_dict = mod.list_to_dictionary(list1_test)

    assert list_dict == list_dict_test

def test_similarity_score():

    ss = mod.similarity_score(list1_test, list2_test)

    assert ss == 31

