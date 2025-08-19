"""
Lists are one of the most heavily used datatypes in Python. 
They are designed to store multiple other Python datatypes such as numbers, strings, and any other type. 
For today’s task, you need to process the following two lists:

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

.Place the two lists in a .py file.

.Add some code that combines the two lists into one single list.

.Removes any duplicates from the combined list.

.Sort the combined list in ascending order.

.Print out the sorted list.
"""

def combine_and_sort_lists(list1, list2):
    """Combine two lists, remove duplicates, and sort the result."""
    combined_list = list1 + list2
    unique_list = list(set(combined_list))
    unique_list.sort()
    return unique_list

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

print(combine_and_sort_lists(list1, list2))