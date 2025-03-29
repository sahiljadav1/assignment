# • Write a generator function that generates the first 10 even numbers. 

def gen():  
    for i in range (2,22,2):
        yield i

for i in gen():
    print(i)

