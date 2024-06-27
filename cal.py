def get_user_input():
    a = input("Enter first number: ")
    print(a)
    if(a=='#'):
        return -1
    try:
        fa=float(a)
    except ValueError:
        return None
    b = input("Enter second number: ")
    print(b)
    if(b=='#'):
        return -1
    try:
        fb=float(b)
    except ValueError:
        return None
    return fa,fb
   
def add(a,b):
    print(float(a), "+", float(b), "=", float(a)+float(b))
    return
   
def subtract(a,b):
    print(float(a), "-", float(b), "=", float(a)-float(b))
   
def multiply(a,b):
    return a*b
   
def divide(a,b):
    try:
        print(float(a), "/", float(b), "=", float(a)/float(b))
    except ZeroDivisionError:
        print("float division by zero")
        print(float(a), "/", float(b), "=", "None")
    except ValueError:
        pass
    return
   
def power(a,b):
    return a+b
   
def remainder(a,b):
    return a+b


def select_op(choice):
    if(choice == "#"):
        return -1
    elif(choice == "+"):
        Z = get_user_input()
        if(Z==None):
            return
        elif(Z==-1):
            return -1
        a,b = Z
        add(a,b)
    elif(choice == "-"):
        Z = get_user_input()
        if(Z==None):
            return
        elif(Z==-1):
            return -1
        a,b = Z
        subtract(a,b)
    elif(choice == "/"):
        Z = get_user_input()
        if(Z==None):
            return
        a,b = Z
        divide(a,b)



while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
 

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()





