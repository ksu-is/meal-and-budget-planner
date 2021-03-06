from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')

#recipe list  = name, cost per serving, and ingredients
rec1 = ["baked potato",2.50,'potato','butter','cheese','bacon']
rec2 = ["spaghetti",4.50,'spaghetti noodles','tomato sauce','hamburger']
rec3 = ["grilled chicken",4.00,'chicken breast','marinade','rice','vegetables']
rec4 = ["cajun pasta",4.50,'shrimp','pasta noodles', 'vodka cream sauce']
rec5 = ["chicken noodle soup",3.50,'chicken broth','vegetables','egg noodles']
rec6 = ["grilled cheese and tomato soup",3.00,'bread','butter','cheese','tomato soup']
rec7 = ["chicken parmesan",5.00,'chicken breast','parmesan cheese','pasta noodles','pesto']

#list of recipe
recipes = [rec1,rec2,rec3,rec4,rec5,rec6,rec7]

week = ["mon","tues","wed","thur","fri","sat","sun"]

#user info
user_budget = []#int(input('What is you budget for the week? '))
user_servings = []#int(input('How many people are you feeding? '))

#user choices
mon_meal = ""

#print all the recipe available
#print('choose from the available recipes')
#for list in recipes:
    #print(list[0])

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
#for day in week:
    #meal = input("Meal - Select from list: ")
    #for list in recipes:
        #if list[0] == meal.lower():
            #print(list[1])
            #meal_cost = list[1] * int(user_servings)
            #print(meal_cost)
            #total_cost += meal_cost
            #print(total_cost)
            #grocery_list.append(list[2::])
            #print("budget remaining", int(user_budget)-total_cost)
        #else:
            #pass
    
#print("total cost for the week:",total_cost)
#print("grocery list",grocery_list)
#budget_dif = 0
#def week_budget():
    #if request.method == 'POST':
        #for key,value in result.items():
            #for list in recipes:
                #if value == list[0]:
                    #total_cost += list[1] * user_servings
                    #budget_dif = user_budget - list[1] * user_servings
                #else:
                    #pass

### this is the form
@app.route('/')
def userform():
   return render_template('userform.html',recipes=recipes,user_budget=user_budget, user_servings=user_servings) #tells which var to pass to html

### this is the table on the next page
@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST': #when submit button is pressed
      result = request.form #remove if test fails
      budget = request.form['user_budget'] # gets user input and save it to py
      mon_meal = request.form['mon_meal']
      return render_template("result.html",result = result, user_budget=user_budget, user_servings=user_servings, recipes=recipes, meal_cost=meal_cost,total_cost=total_cost,grocery_list=grocery_list, mon_meal=mon_meal,) 
                                #result.html
#Testing for budget calcs 
#@app.route('/result',methods = ['POST','GET'])
#def budget_pie():
    #if request.method == 'POST':
        #total_cost = 0
        #result = request.form
        #user_budget = request.form['user_budget']
        #user_servings = request.form['user_servings']
        #budget_dif = 0
        #for key,value in result.items():
           #for list in recipes:
                #if value == list[0]:
                    #total_cost += list[1] * user_servings
                    #budget_dif = user_budget - list[1] * user_servings
                #else:
                    #pass
    #return str(week_budget(int(result.user_budget)))
if __name__ == '__main__':
   app.run(debug = True)
