def calculator():
    
    owner="Terrence"
    
    print("Welcome to "+owner+"Calculator program")
    
    print("Select operation")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    
    while True:
        #get user input
        choice = input("Enter choice(1/2/3/4)\n")
        
        num1 = float(input("Enter the first number\n"))
        num2 =  float(input("Enter the second number\n"))
        
        if choice =="1":
            print(num1+num2)
        
        elif choice=="2":
            print(num1-num2)
        
        elif choice=="3":
            print(num1*num2)
        
        else:
            if num2==0:
                print("Error:Division by zero")
            else:
                print(num1/num2)
        
        break
    
    else:
        print("Invalid input")    
calc=calculator()
print(calc)