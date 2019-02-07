#8. Pickled Vegetables
#Write a program that keeps vegetable names and prices in a dictionary as key-value pairs.
#The program should display a menu that lets the user see a list of all vegetables and their
#prices, add a new vegetable and price, change the price of an existing vegetable, and delete
#an existing vegetable and price. The program should pickle the dictionary and save it to a
#file when the user exits the program. Each time the program starts, it should retrieve the
#dictionary from the file and unpickle it.
import pickle
def addVege(vegetables):
    print()
    print('Add a vegetable to the list.')
    vegetableName = input('Name: ').lower()
    if vegetableName not in vegetables:
        vegetablePrice = float(input('Price: '))
        vegetables[vegetableName] = vegetablePrice
        print(vegetableName, 'was succesfully added to the list.')
    else:
        print('This entry already exists.')

def showList(vegetables):
    print()
    print('List of Vegetables')
    print('------------------')
    for key,value in vegetables.items():
        print(key,':',value)
def changePrice(vegetables):
    print()
    print('Which vegetable price would you like to change?')
    vegetableName = input('Name: ').lower()
    if vegetableName in vegetables:
        vegetablePrice = float(input('New price: '))
        vegetables[vegetableName] = vegetablePrice
        print('Vegetable price has been succesufully updated.')
    else:
        print('This entry does not exist in the list.')

def delVege(vegetables):
    print()
    print('Which vegetable would you like to delete? ')
    vegetableName = input('Name: ').lower()
    if vegetableName in vegetables:
        del vegetables[vegetableName]
        print(vegetableName, 'was deleted.')
    else:
        print('This entry does not exist in the list.')
        
def menu():
    vegetablePrices = dict()
    choice = 0
    try:
        infile = open('data.dat','rb')
        vegetablePrices = pickle.load(infile)
        infile.close()
    except:
        'No save file. Creating a new one.'
        
    while choice != 5:
        print('Menu')
        print('----')
        print('1. Show the list of vegetables')
        print('2. Add a new vegetable')
        print('3. Change the price of a vegetable')
        print('4. Delele a vegetable.')
        print('5. Exit the program.')
        choice = int(input('Make a choice from 1-5: '))
        if choice < 1 or choice > 5:
            print('Not a valid choice.')
            print()
        elif choice == 1:
            showList(vegetablePrices)
        elif choice == 2:
            addVege(vegetablePrices)
        elif choice == 3:
            changePrice(vegetablePrices)
        elif choice == 4:
            delVege(vegetablePrices)
    
    outfile = open( 'data.dat' , 'wb' )
    pickle.dump(vegetablePrices,outfile)
    outfile.close()
menu()