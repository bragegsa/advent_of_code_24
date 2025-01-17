import pandas as pd
import modules.day2_lib as mod

data_list_test = [[7, 6, 4, 2, 1], 
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9]]
    

def test_import_data():

    data_list = mod.import_data_day2('inputs/inputs_test/day2_test.csv')

    assert data_list == data_list_test

def test_check_if_list_safe():

    is_safe_test = [True, False, False, False, False, True]
    is_safe = []

    for row in data_list_test:

        is_safe.append(mod.check_if_list_safe(row))

    assert is_safe == is_safe_test

def test_number_of_safe_reports():

    number_of_safe_reports_test = 2
    number_of_safe_reports = mod.number_of_safe_reports(data_list_test)

    assert number_of_safe_reports == number_of_safe_reports_test

def test_problem_dampener():

    is_safe_test = [True, False, False, True, True, True]
    is_safe = []

    for row in data_list_test:

        is_safe.append(mod.problem_dampener(row))

    assert is_safe == is_safe_test

def test_number_of_safe_reports_with_dampener():

    number_of_safe_reports_test = 4
    number_of_safe_reports = mod.number_of_safe_reports(data_list_test, use_problem_dampener=True)

    assert number_of_safe_reports == number_of_safe_reports_test