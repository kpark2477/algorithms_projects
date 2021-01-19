def sort_012(input_list):

    current_index = 0
    index_for_0 = 0
    index_for_2 = len(input_list) - 1

    while current_index <= index_for_2:
        if input_list[current_index] == 0 :
            input_list[current_index] = input_list[index_for_0]
            input_list[index_for_0] = 0
            index_for_0 += 1
            current_index += 1
        elif input_list[current_index] == 1 :
            current_index += 1
        else:
            input_list[current_index] = input_list[index_for_2]
            input_list[index_for_2] = 2
            index_for_2 -= 1
 
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0]) #edge case
test_function([0]) #edge case