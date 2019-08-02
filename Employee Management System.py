print ("Welcome to Employees Management System")

play = True

my_empty = []
while play:

    my_list =["""
            Employee Management System by Martin Gamban
*********************************************************************************
            Choose your Option:
            [1] Add New Employee
            [2] Enter Hourly Employee
            [3] Show Employee Information
            [4] Exit/Quit
*********************************************************************************
        """]
    print(my_list)

    num = (input("Enter number: ")).lower()

    if num == "1":
        name = (input("Enter Name: ")).lower()
        my_empty.append(name)
        print(name)

        department = (input("Enter Department: "))
        my_empty.append(department)
        print(department)

        position = (input("Enter Position: "))
        my_empty.append(position)
        print(position)

        rate = (input("Enter Rate: "))
        my_empty.append(rate)
        print(rate)
        
    elif num == "2":
        emplonum = (input("Employee Number: "))
        empHours = (input("Employee Hours: "))
        print(empHours.getSalary)
        
    elif num == "3":
        print(my_empty)
        print(e.name, e.department, e.position, e.rate)
        
    elif num == "4":
        print("Goodbye!")
        ans = None
        play = False
    else:
        play = True
