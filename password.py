import string

#define charactet sets
symbols = set(string.punctuation)
numbers = set(string.digits)

#get the user input
username = input("Enter the user name:")
user_password = input("Enter the password:")

#Ensure the password contains at least one symbol or alteast one letters
#password.append(random.choice(symbols))
#password.append(random.choice(letters))

#define desired password legth
length =8


# check the password lenght atleast 8 characters

if len(user_password)<8:
    print("Password must be 8 characters")
else:
    contains_symbols = any(char in symbols for char in user_password)
    contains_numbers = any(char in numbers for char in user_password)

    if not contains_symbols:
        print("passord must contains symbols")
    elif not contains_numbers:
        print("password must contains numbers")
    else:
        print("Uername and password are valid")


"""sample outout
== RESTART: C:/Users/kumar/AppData/Local/Programs/Python/Python312/password.py =
Enter the user name:kumar
Enter the password:kumar@
password must contains numbers

== RESTART: C:/Users/kumar/AppData/Local/Programs/Python/Python312/password.py =
Enter the user name:kumar
Enter the password:kuma1@
Uername and password are valid # wrong functions

== RESTART: C:/Users/kumar/AppData/Local/Programs/Python/Python312/password.py =
Enter the user name:Kumar
Enter the password:kuma1@
Password must be 8 characters

== RESTART: C:/Users/kumar/AppData/Local/Programs/Python/Python312/password.py =
Enter the user name:kumar
Enter the password:kuma@1rt
Uername and password are valid  """
