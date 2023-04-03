print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

''')
menu ={
    "Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
}

order = {}

while True:
    user_input = input("> ")
    
    if user_input == "quit":
        print(f"This Is Your order {order}")
        break
        
    elif user_input in [item for sublist in menu.values() for item in sublist]:
        
        if user_input not in order:
            order[user_input] = 1
        else:
            order[user_input] += 1
            
        count = order[user_input]
        
        if count == 1:
            print(f"** 1 order of {user_input} has been added to your meal **")
        else:
            print(f"** {count} orders of {user_input} have been added to your meal **")
    
    else:
        print("** Please enter a valid menu item **")
