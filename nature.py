#welcome our users
print("Hello and welcome to our nature walk center")
#set an initial choice value
choice = int(input("Where would you like to start? Press 1- to start the walk,2- to customize your walk before you start,3-If you would like more info and our contacts or 4-If you would like to close the program\n"))
#redirect to respective places
if choice == 1:
    print("Your walk begin now")
elif choice == 2:
    Setting=int(input("What would you like to customize about your walk? Press 1-Weather,2-Time,3-Location\n"))
    if Setting == 1:
            Weather=int(input("Press 1 for sunny,2 for cloudy,3 for rainy\n"))
            if Weather== 1 or 2 or 3:
                print("Your walk will have the weather selected")
    elif Setting == 2:
            Time=int(input("Press 1 for morning,2 for afternoon,3 for evening\n"))
            if Time== 1 or 2 or 3:
                print("Your walk will have the time selected")  
    elif Setting == 3:
            Location=int(input("Press 1 for Kenya,2 for Ethiopia\n"))
            if Location== 1 or 2:
                print("Your walk will have the location selected")
elif choice == 3:
    print("You will be redirected to our contacts page")        
else:
    print("Thank you and Goodbye")