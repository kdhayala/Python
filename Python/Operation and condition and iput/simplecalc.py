#merging main
total_times = 2
while total_times > 0:
    total_times = total_times - 1
    print("Simple calculator")
    print("1. Addition")
    print("2. subraction")
    print("3. mutipication")
    print("4.divison")
    print("5. Modulus")
    print("6. Exponentiaate")
    choice =input("Enter your choice (1/2/3/4/5/6): ")
    num1 = float(input("Enter the number 1: "))
    num2 = float(input("Enter the number 2: "))
    if (choice=="1"):
        result = num1 + num1
        print(result)
    elif(choice=="2"):
            result = num1 - num2
            print(result)
    elif(choice=="3"):
        result = num1 *  num2
        print(result)
    elif(choice=="4"):
        result = num1 / num2
        print(result)
    elif(choice=="5"):
        result = num1 % num2
        print(result)
    elif(choice=="6"):
        result = num1 ** num2
        print(result)
    else:
        print("Option is not valid")
                        

