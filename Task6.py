def get_min_max(ints):
    min = ints[0]
    max = ints[0]

    for i in ints:
        if ints[i] < min:
            min = ints[i]
        if ints[i] > max:
            max = ints[i]

    return (min, max)


## Example Test Case
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1)]  # a list only containing 0, edge case
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1000001)]  # a list containing 0 - 1000000, edge case
random.shuffle(l)

print ("Pass" if ((0, 1000000) == get_min_max(l)) else "Fail") 
