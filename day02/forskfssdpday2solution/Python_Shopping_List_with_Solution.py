# Shopping List App 

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app

    Step 6: print out the list
"""


#   Make a list to hold onto our items.
shopping_list = []

# Print out instructions on how to use the app
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    
    # add new items to our list
    shopping_list.append(new_item)

#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )



"""
Challenge 2
    If I type SHOW, 
    I should be able to see what is currently in the list

    If I type HELP, 
    I should be able to see all the help for these special commands

Hint 2
    Step 1: Have a HELP command
    Step 2: Have a SHOW command
    Step 3: Add a function for adding into the list 
    Step 4: Cleanup the code in general
"""

# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print ( "What should we pick up at the store ? ")

    print ( """
       Enter 'DONE' to stop adding items. 
       Enter 'HELP' for this help. 
       Enter 'SHOW' to see your current list. 
       """)

def show_list():
    #  print out the list
    print("Here's your list")
    for item in shopping_list:
        print ( item )

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print ("Added {}. List now has {} items.".format(new_item, len(shopping_list)))



# call the show_help function before the while loop starts 
show_help()


# ask for new items
while True:
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    else :
        add_to_list(new_item)


"""

Challenge 3
    User can enter SHOW or Show or show, 
    similar for DONE and HELP, but the program should do the required job

    Show the item in the list serially starting from 1

    Let us accept items using a comma separated string
        
    Also there should be a functionality to add an item at a specific index

    There should be a functionality to remove items from the list at a specific index using REMOVE
    
    Do all the exception handling for all the extreme use cases 
"""


# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print ( "What should we pick up at the store ? ")

    print ( """
       Enter 'DONE' to stop adding items. 
       Enter 'HELP' for this help. 
       Enter 'SHOW' to see your current list. 
       """)

def show_list():
    #  print out the list
    print("Here's your list")
    for index,item in enumerate(shopping_list):
        print ( index, item )

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print ("Added {}. List now has {} items.".format(new_item, len(shopping_list)))


def remove_item (idx):
    index = idx -1 
    item = shopping_list.pop(index)
    print ( "Remove {}". format(item))

# call the show_help function before the while loop starts 
show_help()


# ask for new items
while True:
    new_item = input("> ").upper()

    # be able to quit the app
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == 'REMOVE' :
        show_list()
        idx = input("Which item ? Tell me the number ")
        remove_item(int(idx))
        continue 
    else :
        new_list = new_item.split(",")
        index = new_item(" Add this at a certain spot? Press enter for the end of the list or give me a number "
                         + " Currently {} items in the list ". format(len(shopping_list)))
        if index:
            spot = int(index) - 1
            for item in new_list :
                shopping_list.insert(spot,item.strip())
                spot +=1 
        else:
            for item in new_list:
                shopping_list.append(item.strip())

"""
Challenge 4   
    Do all the exception handling for all the extreme use cases 
"""

"""
Challenge 5   
    Store the shopping list in a file. 
"""
