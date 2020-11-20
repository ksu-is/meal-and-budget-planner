from flask import Flask, render_template, request
app = Flask(__name__)

#recipe list  = name, cost per serving, and ingredients
rec1 = ["baked potato",2.50,'potato','butter','cheese','bacon']
rec2 = ["spaghetti",2.00,'spaghetti noodles','tomato sauce','hamburger']
rec3 = ["grilled chicken",1.50,'chicken breast','marinade']

#list of recipe
recipes = [rec1,rec2,rec3]

week = ["mon","tues","wed","thur","fri","sat","sun"]

#user info
user_budget = int(input('What is you budget for the week? '))
user_servings = int(input('How many people are you feeding? '))

#print all the recipe available
print('choose from the available recipes')
for list in recipes:
    print(list[0])

#set up peramiters
meal = ""
meal_cost = 0
total_cost = 0
grocery_list = [] #<----figure out how to remove duplicates and add multiples
#for each day of the week select a meal from the printed recipe list
#for each list in the recipes list look for the selected meal
#when true choose the second list item ie the cost and multiply by the user_servings
#add the meal cost to the total cost
#add the ingredents to the grocery list
for day in week:
    meal = input("Meal - Select from list: ")
    for list in recipes:
        if list[0] == meal.lower():
            #print(list[1])
            meal_cost = list[1] * int(user_servings)
            #print(meal_cost)
            total_cost += meal_cost
            #print(total_cost)
            grocery_list.append(list[2::])
            print("budget remaining", int(user_budget)-total_cost)
        else:
            pass
    
print("total cost for the week:",total_cost)
print("grocery list",grocery_list)



