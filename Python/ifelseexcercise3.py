""" get a input for score percenatge, only of the percentage is greater than 70,
get input his namee, departement and location. then print your are eligible, if not
print you are not eligible


score=int(input("Score Percentage"))
if(score>70):
    name=input("Enter your name")
    department=input("Enter your department")
    location=input("enter your location")
    print("you are eligible")
else:
    print("you're not eligible")

    

# if salary greater than or equal to 20000 or age less than or equal to 25/ get input
# for required loan amount, if not print you're not eligible for loan
#nested if
salary=int(input("Enter your salary"))
age=int(input("Enter your age"))
if(salary>=20000 or age <=25):
    loan_amount=int(input("Enter the loan amount"))
    if(loan_amount>50000):
        print("maximum loan amout is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you're not eligible for loan")
    
"""
#9. Get input for five subject marks, add all of it, and find average. if average mark is less than
#mart less than 35, print""Additional class is required" else print you are good to go


tamil=int(input("Enter tamil mark:"))
english=int(input("Enter English mark:"))
maths=int(input("Enter maths mark:"))
science=int(input("Enter science mark:"))
social=int(input("Enter social mark:"))
total=(tamil+english+maths+science+social)/5
if(total>35):
    print("you are good to go")
else:
    print("Additional class is required")
