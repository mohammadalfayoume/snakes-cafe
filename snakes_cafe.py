# print("hello")
from pickle import FALSE

print('''**********************************************
**      Welcome to the Snackes Cafe!        **
**      Please see our manu below.          **
**
**  To quit at any time, type "quit"        **
**********************************************''')
menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
}

for item in menu:
    print(item)
    print("-"*len(item))
    for i in menu[item]:
        print(i)
    print("\n")


print('''**********************************
** What would you like to order **
**********************************''')
condition = True
counter = 1
collection = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
              "A Literal", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
dictionary={}
while condition:
    order = input(">")
    if order in collection:
        if order in dictionary:
            print(f"** {dictionary[order]+1} order of {order} have been added to your meal **")
            dictionary[order] +=1
        else:
            print(f"** 1 order of {order} have been added to your meal **")
            dictionary[order]=1 
    else:
        print("sorry, we don't have this order!")   
    if order == "quit":
        print("GoodBye^^")
        condition = False