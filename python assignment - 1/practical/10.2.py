# • Write a Python program that uses reduce() to find the product of a list of numbers. 
 
from functools import reduce

l1 = [1,2,3,4,5,6]

result = reduce(lambda num1,num2 : num1 * num2 , l1 )

print(result)