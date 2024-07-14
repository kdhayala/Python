name = "kumar"
password = "123"
bal = 2000
a=input("Enter the name")
b=input("Enter the password")
if(a==name and b==password):
    print("print 1 for deposit \1 print 2 for withdrawal \n print 3 for check current balance")
    c=int(input("Entet the number"))
    if(c==1):
        d=int(input("Enter the deposit amount"))
        if(d>20000):
            print("limit upto 20000")
        else:
                print("desposited successfully")
                bal=bal+d
                print("Current balance",bal)
    elif(c==2):
        e=int(input("Enter the withdrawal amout"))
        if(e<bal):
            print("withdraw successfully")
            bal=bal-e
            print("The current balace",bal)
        else:
            print("The balance exceed")


    elif(c==3):
        print("The current balace",bal)
        print("Thank you")
else:
    print("Invalid")
                    
          
                
