# Practical Example 6: Write a Python program to check if a number is prime using if_else. 


num = int(input("Enter a number: "))

status = True

for i in range (2,num):
    if num % i == 0:
        status = False 
        break  

    if status:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
