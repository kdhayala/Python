
""""number=int(input("Enter the number:"))
if(number%2==0):
    print("This is even number")
else:
    print("This is the odd  number")


Get the score of  out of 100

<35 = poor student
35 inbetween 70 = average student
>70 = Good Student

If statement going to check the all the statements.

score=int(input("Enter the mark:"))
if(score<35):
    print("poor student")
if(score>35 and score<75):
    print("Average student")
if(score>70):
    print("Good student")

And = true * true = true
or =  true * false = true






# If condition is true program needs to be stopped, so that we are going to use elif

# if we used else: statement we are unable anyother if statements.

score=int(input("Enter the mark:"))
if(score<35):
    print("poor student")
elif(score>35 and score<75):
    print("Average student")
elif(score>75 and score<100):
    print("Good student")
else:
    print("invalid number")
    """


## Mini calculator
a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/div:")
if(operation== "add"):
    print(a+b)
elif(operation== "sub"):
    print(a-b)
elif(operation== "div"):
    print(a/b)
elif(operation== "mul"):
    print(a*b)
else:
    print("invalid number")
