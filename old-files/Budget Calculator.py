meal_choice = {}
meal_history = {}
stop = 'go'
while stop != 'q'
    item_name = iput('Meal choice: ')
    quantity = input("Total purchased: ")
    meal_choice['name'] = item_name
    meal_choice['number'] = int(quantity)
    meal_choice['price'] = float(cost)
    meal_history.append(meal_choice.copy())
    stop = input("Would you like to choose a different meal?\nType 'c' for continue or 'q' to quit :")
final_total = 0
for index, item in enumerate(meal_history):
    item_total = item['number'] * item['price']
    final_total += item_total
    print(item['number'], item['name'], item['price'], item_total))
    item_total = 0
print('Grand total: $%.2f' % final_total)

recommendation_budget = 0

def program():
    print()
    print('Basic Recommended Budget From Chime.com' ) 

    budget_program = 'Recommendation Budget'
    your_budget = recommendation_budget
    while budget_program == 'Recommendation Budget':
        print()
        print('YOUR RECOMMENDED BUDGET CATEGORY PERCENTAGES!')        
        print('Housing is 25%:\n $', format(round(your_budget *.25,2), '.2f'))
        print('Food is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Transportation is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Utilities is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Personal is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print()
        print('Menu:')
        print('1 to Add your income: ')
        print('Q to Quit')
        menu_options = input('Select 1 or Q: ')
        if menu_options == '1':
            your_budget = add_income(your_budget)
        elif menu_options == 'q':
            print()
            print('Goodbye!')
            print()
            break
        elif menu_options == 'Q':
            print()
            print('Thank You!')
            print()
            break
        else:
            print()
            print('Invalid selection, please select 1 or Q')

def add_income(your_budget):
    print()
    income = float(input('Enter income: $'))
    your_budget = income
    if your_budget >= 1:
        return your_budget
    else:
        print('Please enter amount over $1')
        return add_income(your_budget)

program()
