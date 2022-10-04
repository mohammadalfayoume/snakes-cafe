import collections
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

collection = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado',
              'a literal', 'ice cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

print('''**********************************
** What would you like to order **
**********************************''')


def get_orders():
    dictionary = {}
    order = ''
    while order != 'quit':
        order = input('>').lower()
        if order == 'quit':
            print('Your orders are being preparing')
            break
        if order not in collection:
            print(f"sorry, we dont have {order}")
            continue
        else:
            if order in dictionary:
                dictionary[order] += 1
            else:
                dictionary[order] = 1

        if len(dictionary) == 1:
            print(
                f'{dictionary[order]} order of {order} has been added to your order')
        else:
            temp = ''
            temp +=' and '.join(f'{value} order of {key}' for key, value in dictionary.items())
            print(f"{temp} have been added to your order")
            
    print('''
    **************************************
    **😋This is summary of your order😋**
    **************************************
    ''')
    str = ""
    str +=' and '.join(f"{value} order of {key}" for key, value in dictionary.items())
    print(str)


get_orders()
