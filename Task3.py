def mergesort(arry):

    if len(arry) <= 1:
        return arry
    
    mid = len(arry) // 2
    left = arry[:mid]
    right = arry[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):

    if len(input_list) <= 1:
        return "we need at least 2 elements to form 2 numbers!"

    sorted_list = mergesort(input_list)
    max1 = ''
    max2 = ''

    for index, element in enumerate(sorted_list):
        if index == 0 or index // 2 == index / 2:
            max1 = max1 + str(element)
        else:
            max2 = max2 + str(element)

    return [int(max1), int(max2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)
test_case_2 = [[1, 6, 3, 5, 9, 8], [963, 851]]
test_function(test_case_2)
test_case_3 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_3)
test_case_4 = [[7, 7, 7, 7, 7, 7], [777, 777]] # edge case
test_function(test_case_4)

print("Pass" if (rearrange_digits([]) == "we need at least 2 elements to form 2 numbers!") else "Fail") # edge case