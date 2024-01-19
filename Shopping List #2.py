#Shopping List
#Morgan and Steph


#Initialize
shoppingList = []


#Functions
#asks user for item to add to list
#adds item and prints list
def addItems():
   additems = input("Please add an item you would you like to add to your list: ")
   shoppingList.append(additems)
   print(shoppingList)


#prints the user's shopping list
def viewList():
   print(shoppingList)


#asks user for item to mark as completed
#finds index and places check next to item
def markDone():
   completedtask = input("Which item would you like to mark as completed?: ")
   i = shoppingList.index(completedtask)
   shoppingList[i] = completedtask + " X "
   print(shoppingList)


#asks user for item to remove from list
#removes item and prints list
def removeItem():
   takeitems = input("Which items would you like to remove from your shopping list?: ")
   shoppingList.remove(takeitems)
   print(shoppingList)


#Option 5 : Allows users to Clear the entire list of notes. This operation is useful for starting fresh or when the user wants to delete all notes at once.
def clearList():
   print("Clearing items from list... ")
   shoppingList.clear()
   print("You successfully cleared your list!")
   print(shoppingList)
  
#Option 6 : Implement the ability to sort the list in alphabetical order.
def sortList():
   print("Now sorting list in alphabetical order...")
   shoppingList.sort()
   print("Your list is now in alphabetical order!")
   print(shoppingList)


#Option 7 : Provide an option that counts and displays the total number of notes currently in the list.
def countList():
   print("Counting the number of items in your list...")
   size = str(len(shoppingList))
   print("You have " + size + " items in your list!")
  
#Main
while True:
   print("\nWelcome to your shopping list. Please choose which operation you would like to perform: ")
   print("1. Add an item to the shopping list \n2. View the current shopping list \n3. Mark an item as completed \n4. Remove an item from the shopping list \n5. Clear shopping list \n6. Sort shopping list in alphabetical order \n7. Count number of items in the shopping list \n8. Exit the program ")
   option = int(input("\nOption: "))
   if option == 1:
       addItems()
   if option == 2:
       viewList()
   if option == 3:
       markDone()
   if option == 4:
       removeItem()
   if option == 5:
       clearList()
   if option == 6:
       sortList()
   if option == 7:
       countList()
   if option == 8:
       print("Thank you for using EZ Shopping List! Goodbye.")
       break
