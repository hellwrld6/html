def calculator():
    num1= float(input("Enter the first number\n"))
    operator=input("Enter the operation you would like to carry out?\n")
    num2=float(input("Enter the second number\n"))
        
    if operator=="+":
        def Add():
            print(num1+num2)
        Add()
    elif operator=="-":
        def subtract():
            print(num1-num2)
        subtract()
    elif operator=="*":
        def multiply():
            print(num1*num2)
        multiply()
    elif operator=="/":
        def Divide():
            print(num1/num2)
        Divide()
    else:
        def Wronginput():
            print("INVALID OPERATOR.TRY AGAIN!")
        Wronginput()
        
calculator()