import pandas as pd

from modules import import_data_day2, number_of_safe_reports

def run_day2():

    print("\n--- Day 2 ---")

    data_list = import_data_day2()
    print(f'The number of safe reports is: {(number_of_safe_reports(data_list))}')
    print(f'The number of safe reports with Problem Dampener is: {(number_of_safe_reports(data_list, use_problem_dampener=True))}')


if __name__ == "__main__":
    
    run_day2()
