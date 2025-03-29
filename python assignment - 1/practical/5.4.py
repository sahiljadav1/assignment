"""
Practical Example 4: Print this pattern using nested for loop: 
markdown 
Copy code 
* 
** 
*** 
**** 
*****
"""

row = 5

for i in range(1, row + 1):
    for j in range(i):
        print(" * ", end="")  
    print()  
