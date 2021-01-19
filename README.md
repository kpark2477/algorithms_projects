# algorithms_projects
Udacity 자료구조 알고리즘 코스의 알고리즘 프로젝트입니다.
총 7가지 문제로 구성이 되어있고, 주어진 문제에 맞추어 알고리즘을 구현하는 문제입니다.
(binary search, heapify, trie, mergesort, quicksort, divide and conquer 등의 개념을 다룹니다.)


개별문제 해답에 대한 디자인과 time complexity는 
[`./explanation.md`](./explanation.md) 에서 확인하실 수 있습니다.

문제 내용은 아래와 같습니다.

## 1.Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))
Here is some boilerplate code and test cases to start with:

## 2.Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## 3.Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.

## 4.Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.


## 5.Autocomplete with Tries
we need to add the ability to list suffixes to implement our autocomplete feature. 
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. 
For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, 
we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

## 6.Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

## 7.HTTPRouter using a Trie
First we need to implement a slightly different Trie than the one we used for autocomplete. 
Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. 
In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler 
which would be responsible for handling requests to that path. For the sake of simplicity 
we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, 
but this would result in a Trie with a very large number of nodes and lengthy traversals 
if we have a lot of pages on our site. A more sensible way 
to split things would be on the parts of the path that are separated by slashes ("/"). 
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
We really just need to insert and find nodes, 
and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

Next we need to implement the actual Router. 
The router will initialize itself with a RouteTrie for holding routes and associated handlers. 
It should also support adding a handler by path and looking up a handler by path. 
All of these operations will be delegated to the RouteTrie.
