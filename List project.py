#List Project
#Brandon Sino
#1/10/24


List = [" "]

def Additem(food) : 
    List.insert(0 , food )
    return List

def removeitem(takeout) :
    List.pop(takeout)
    return List

def markcompleted(check , name):
    List[check] = name + "X"
    return List

def sortAlphabetically():
    List.sort()

def clearList():
    List.clear()
    

def numberofitems():
    print(len(List))
    return List
    
    
def ListMenu():
    print("Welcome to the List Menu")
    print("Please choose an operation: (type in a number between 1 - 5)")
    print( "1. Add to List \n2. View List \n3. Mark Task Completed  \n4. Remove a Task \n 5. Quit the Program \n 6. Sort the list alphabetically \n 7. Clear the list \n  8. Show number of items in list" )
    option = int(input("Option: "))

    if option == 1:
        food = (input ("what item would you like to add to the list? "))
        print(Additem(food))
        ListMenu()
        
    if option == 2:
        print(List)
        ListMenu()

    if option == 3:
        check = int(input("what is the position of the item would you like to mark as completed?"))
        name = (input("what is the name of the item you want to mark completed?"))
        print(markcompleted(check, name))
        ListMenu()
    
    
    if option == 4:
        takeout = int(input("what item would you like to remove from the list? "))
        print(removeitem(takeout))
        ListMenu()
    
    if option == 5:
        quit()

    if option == 6: 
        sortAlphabetically()
    
    if option == 7:
        clearList()
    
    if option == 8:
        numberofitems()




ListMenu()