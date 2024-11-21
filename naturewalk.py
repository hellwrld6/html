print("Welcome to our nature walk.What would like to do?")
choices = ''
while choices != "q":
    print("[1]Enter 1 to go for bicycle ride\n")
    print("[2]Enter 2 to go for run\n")
    print("[3]Enter 3 to climb a mountain\n")
    print("[4]Enter 4 to quit")
    
    choices =  (input("What would you like to do?\n"))
    
    if choices == 1:
        print("Here is a bicycle,have fun")
    elif choices== 2:
        print("Here are some running shoes, Enjoy the run")
    elif choices == 3:
        print("Here is a map, Climb to the peak")
    elif choices == 4:
        print("Thank you for stopping by , Have a nice day")
    else:
        print("I dont understand, please try again")
    
print("We are all done now , Enjoy your day,Bye!")
        
