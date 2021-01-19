def rotated_array_search(input_list, number):
    end_index = len(input_list) - 1
    return arry_search_range(input_list, 0, end_index, number)
    

def arry_search_range(input_list, start_index, end_index, number):
    if (end_index - start_index) <= 1:
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1
    mid_index = (start_index + end_index)//2
    if input_list[mid_index] < number:
        if input_list[mid_index] < input_list[end_index] < number:
            return arry_search_range(input_list, start_index, mid_index, number)
        else:
            return arry_search_range(input_list, mid_index, end_index, number)
    else:
        if number < input_list[start_index] < input_list[mid_index]:
            return arry_search_range(input_list, mid_index, end_index, number)
        else:
            return arry_search_range(input_list, start_index, mid_index, number)

"""
Find the index by searching in a rotated sorted array

Args:
    input_list(array), number(int): Input array to search and the target
Returns:
    int: Index or -1
"""


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1], 1]) # edge case
test_function([[], -1]) # edge case