### Task1
## Design:
- If we try to find the root number, iterating from number 0, it would take time complexity of N
- So the idea is to find the range where there is the answer.
- When we find the range, we increase upper limits exponentailly (base is 2, and increase exponent incrementally)
- And also when we narrow down the range until we reach the answer, we take the half of the range recursively

## Time Complexity:
- O(log(n))
- To set the range, it will take log(n) cause we increase the range 2-based exponentailly.
- And then finding the answer within the range also takes log(n). because we keep taking the range in half.

## Space Complexity:
- O(1)
- We don't need to store data here.



### Task2
## Design:
- We try to achieve time complexity of log(n), So we can't just iterate the whole list.
- So we should split the list in half, and keep doing it. But the problem is there's rotating point.
- So we need this thought process. first we pick the middle element. And then if the target is bigger than the middle element, we check the end element.
- If the end element is smaller than middle element, the target must be between the middle and the end. Because it means the rotating point is also between them.
- Like the above, we keep taking half of the list, and then think about possibilities. 

## Time Complexity:
- O(log(n))
- We keep taking half of the list, so time complexity is log(n)

## Space Complexity:
- O(n)
- We do not create another list. We would just need the space of size of one list input.



### Task3
## Design:
- To make sum of two numbers maximun, we should put the biggest number on biggest digts place. And then put the 2nd biggest number to the second biggest digit place.
- And we should move on until we reach the smallest number.
- After all, this means we should sort the list. And merge sort is known to take nlogn time complexity.

## Time Complexity:
- O(nlog(n))
- mergesort takes nlog(n) time complexity

## Space Complexity:
- O(n)
- To mergesort the list and rearrange them doesn't need more than the size of the input list.




## Task4
## Design:
- To achieve sorting with a single traversing, I implemented a function that iterate through the list only once.
- When the function encounter each item, it moves the item to the right position (zero to front, two to end)

## Time Complexity:
- O(n)
- The function iterate through the input list only once

## Space Complexity:
- O(n)
- Because the function only traverse the list and only change the order of it, It only needs a space of the size of input list.



## Task5
## Design:
- suffixes funtion should return all the suffixes of complete words below that node. 
- I implemented a function that recursively go down all the sub part of a trie and add a word to a list if it hits a complete word.

## Time Complexity:
- O(n^2)
- the function traverse all the last node in the trie. if it's binary tree traversing time would be nlog(n), but for trie, there is no ruld for the way it has its children.
- worst case would be n^2 (to find one word, it needs to go down to nth level)

## Space Complexity:
- O(n)
- it needs to store the found words in a list



## Task6
## Design:
- To find min and max on a single treversing, It should keep track of both of them.
- I constructed both min and max variables, and iterate through the list.

## Time Complexity:
- O(n)
- it iterates through the list only "once"


## Space Complexity:
- O(1)
- it only iterate through the list and doesn't make another list.



## Task7
## Design:
- Trie structure with url adresses
- unlike dictionary type trie takes a single letter, this trie takes chunks of letters which are parts of url.
- Input url should be splited into parts by slashes  


## Time Complexity:
- O(n^2)
- When you lookup a url with n parts divded by slashes, It has to go down nth level, and it needs to traverse each level as it goes down (worst case)

## Space Complexity:
- O(1)
- look up doesn't need additional space.
