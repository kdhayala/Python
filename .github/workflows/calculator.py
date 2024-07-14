def add(x, y):
  return x+y

def subtract(x, y):
  return x-y

def mutiply (x, y):
  return x*y

def division(x, y):
  if  y == 0:
      return   "Error! division by zero"
  return x/y


#Main program
while True:
    print("Select operator")
    print("1. Add")
    print("2. subtract")
    print("3. mutiply")
    print("4. division")
    print("5. exit")
    
    choice = input("Entet the choice (1/2/3/4/5)")
  if choice in ['1'
