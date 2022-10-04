
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



order_list=[] 
collection = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado',
              'a literal', 'ice cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']
index_list=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
while True:
    order=input(">").lower() 
    if order.lower() == 'quit':
        break
    if order not in collection:
        print('Choose from menu, please!!')
        continue
    else:
        if order not in order_list:
            index=collection.index(order) #3
            index_list[index] =1
        else:
            index=collection.index(order) #3
            index_list[index] +=1

        if len(order_list)==0:
            index=collection.index(order) #3
            print(f'{index_list[index]} order of {order} has been added to your meal')
            order_list.append(order)
        else:
            if order in order_list:
                temp = ''
                # order_list.append(order)
                for meal in order_list:
                    index=collection.index(meal) #3
                    temp += f' and {index_list[index]} order of {meal}'
                print(f"{temp[4:]} have been added to your order")
            else:
                temp = ''
                index=collection.index(order)
                order_list.append(order)
                for meal in order_list:
                    index=collection.index(meal)
                    temp += f' and {index_list[index]} order of {meal}'
                print(f"{temp[4:]} have been added to your order")       

print('''
    **************************************
    **😋This is summary of your order😋**
    **************************************
    ''')
temp = ''
for order in order_list:
    temp = ''
    # order_list.append(order)
    for meal in order_list:
        index=collection.index(meal) #3
        temp += f' and {index_list[index]} order of {meal}'
print(f"{temp[4:]} have been added to your order")