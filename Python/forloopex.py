# For loop example i=variable
"""
for i in "apple":
    print(i)


    
# range function  it going to check 0 to before defined number.

for i in range(6):
    print(i)

# 2 tables print...
for i in range(1,21):
    print(i, "x 2 =", i*3)



Get input a and  b  and print the number a and b
sample o/p 8 15
sample o/p 9 10 11 12 13 14 

a=int(input())
b=int(input())
for i in range (a+1,b):
    print(i)  


# print even number 1 to 10

for i in range(1,11):
    if(i%2==0): #Even
        print(i)

for i in range(1,11):
    if(i%2!=0): #ODD
        print(i) 


#count even number 1 to 10
count=0
for i in range(1,5):
    if(i%2==0):
        count=count+1
print(count)


#count odd and even number between 1 to 10

count=0
for i in range(1,10):
    if(i%2==0 or i%2!=0):
        count=count+1
print(count)

"""

count=0
for i in range(1,111):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)

