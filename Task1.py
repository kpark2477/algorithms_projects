def sqrt(number):
   n = 1
   while number >= n*n:
      if number == n*n:
         return n
      else:
         n = n*2
   return find_sqrt_range(n/2, n, number)


def find_sqrt_range(start, end, number):
   mid = (start + end)//2
   if mid*mid == number:
      return mid
   if mid == start:
      if (number - start*start) <= (end*end - number):
         return start
      else:
         return end
   if mid*mid > number:
      return find_sqrt_range(start, mid, number)
   else:
      return find_sqrt_range(mid, end, number)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (8 == sqrt(67)) else "Fail")
print ("Pass" if  (13 == sqrt(170)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail") # edge case
print ("Pass" if  (0 == sqrt(0)) else "Fail") # edge case
print ("Pass" if  (993808 == sqrt(987654321987)) else "Fail") # edge case
