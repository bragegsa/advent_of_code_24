import numpy as np
import re

def format_data(data: list) -> tuple[list, dict]:
    '''
        Returns a list of updates and a dictionary containing the rules for each number

        Args:
            data: list of strings

        Returns:
            updates: list of updates
            rules_dict: dictionary containing rules for each number
    '''

    data_formatted = data.split('\n')
    
    regex_line = '[0-9]{1,2}\|[0-9]{2}'
    rules_non_filtered = re.findall(regex_line, data)

    updates = [x.split(',') for x in data_formatted if x not in rules_non_filtered and x != '']

    number = '[0-9]{2}'
    rules_dict = {}
    for rule in rules_non_filtered:

        numbers = re.findall(number, rule)

        if numbers[0] in rules_dict.keys():

            rules_dict[numbers[0]].append(numbers[1])
        else:
            rules_dict[numbers[0]] = [numbers[1]]

    return updates, rules_dict

def check_updates(updates: list, rules: dict) -> list:
    '''
        Returns a list of correct updates

        Args:
            updates: list of updates
            rules: dictionary containing rules for each number

        Returns:
            result_list: list of correct updates
    '''

    result_list = []

    for i in range(len(updates)):

        reversed_updates = updates[i][::-1]
        break_flag = False

        for j in range(len(updates[i])-1):

            if not break_flag:

                for k in range(j+1, len(updates[i])):

                    if reversed_updates[j] in rules.keys():

                        if reversed_updates[k] in rules[reversed_updates[j]]:

                            result_list.append(False)
                            break_flag = True
                            break

        if not break_flag:

            result_list.append(True)

    return result_list

def result_sum(updates: list, result_list: list) -> int:
    '''
        Returns the sum of middle element of all correct updates

        Args:
            updates: list of updates
            result_list: list of correct updates

        Returns:
            result_sum: sum of middle element of all correct updates
    '''

    result_sum = 0

    for i, result in enumerate(result_list):

        if result:
            
            result_sum += int(updates[i][int(len(updates[i])/2)])

    return result_sum

def incorrect_updates(updates: list, result_list: list) -> list:

    remaining_updates = []

    for i, result in enumerate(result_list):

        if not result:

            remaining_updates.append(updates[i])

    return remaining_updates

def fix_incorrect_update(update: list, rules: dict) -> list:
    '''
        !Recursive function!

        Returns a ordered list based on rules.

        Args:
            update: list of pages
            rules: dictionary containing rules for each number

        Returns:
            new_update: list containing ordered update based on rules
    '''

    reversed_update = update[::-1]
    new_update = reversed_update

    for i in range(len(update)):

        for j in range(i+1, len(update)):

            if reversed_update[i] in rules.keys():
                if reversed_update[j] in rules[reversed_update[i]]:

                    first_priority_page = reversed_update[i]
                    last_priority_page = reversed_update[j]

                    new_update[j] = first_priority_page
                    new_update[i] = last_priority_page

                    new_update = new_update[::-1]
                    new_update = fix_incorrect_update(new_update, rules)

                    return new_update
            

    return new_update[::-1]

def fix_incorrect_updates(remaining_updates: list, rules:list) -> tuple[list, list]:
    '''
        Returns two lists. One is the correctly ordered updates and the other is
        the list of bools showing correctly ordered updates

        Args:
            remaining_updates: list of unordered updates
            rules: dictionary containing rules for each number
        
        Returns:
            fixed_updates: list of ordered updates
            result_list: list of bools showing correctly ordered updates 
    '''

    fixed_updates = []

    for update in remaining_updates:

        fixed_updates.append(fix_incorrect_update(update, rules))

    result_list = [1] * len(fixed_updates)

    return fixed_updates, result_list

def run_day5():
    '''
        This function solves the task for day 3
    '''

    print("\n--- Day 5 ---")

    data = import_data_day3(path='inputs/day5.txt')
    updates, rules = format_data(data)
    results = check_updates(updates, rules)
    print(f'The sum of middle page number of all correctly ordered updates: {result_sum(updates, results)}')
    
    remaining_updates = incorrect_updates(updates, results)
    fixed_updates, results_fixed = fix_incorrect_updates(remaining_updates, rules)
    print(f'The sum of middle page number of all correctly ordered updates: {result_sum(fixed_updates, results_fixed)}')

if __name__ == "__main__":

    from day3_lib import import_data_day3
    
    print("\n--- Running module directly ---")
    run_day5()

else:
    from .day3_lib import import_data_day3