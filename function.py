def calculator():
    while True:
        num1=float(input("Enter a number\n"))
        
        operator=input("Enter an operator i.e +,-,*,/,%\n")
        num2=float(input("Enter another number\n"))
        if operator=="+":
            print(num1+num2)
        elif operator=="-":
            print(num1-num2)
        elif operator=="*":
            print(num1*num2)
        elif operator=="/":
            print(num1/num2)
        elif operator=="%":
            print(num1%num2) 
        else:
            print("Invalid operator")
        break
    
    
calculator()

