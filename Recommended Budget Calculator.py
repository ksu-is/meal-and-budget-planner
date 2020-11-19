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
        print('Insurance is 15%:\n $', format(round(your_budget *.15,2), '.2f'))
        print('Food is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Transportation is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Utilities is 5%:\n $', format(round(your_budget *.05,2), '.2f'))
        print('Savings is 15%:\n $', format(round(your_budget *.15,2), '.2f'))
        print('Entertainment is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
        print('Giving is 10%:\n $', format(round(your_budget *.10,2), '.2f'))
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
