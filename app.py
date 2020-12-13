from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')

#recipe list  = name, cost per serving, and ingredients
rec1 = ["Baked Potato",2.50,'potato','butter','cheese','bacon']
rec2 = ["Spaghetti",4.50,'spaghetti noodles','tomato sauce','hamburger']
rec3 = ["Grilled Chicken",4.00,'chicken breast','marinade','rice','vegetables']
rec4 = ["Cajun Pasta",4.50,'shrimp','pasta noodles', 'vodka cream sauce']
rec5 = ["Chicken Noodle Soup",3.50,'chicken broth','vegetables','egg noodles']
rec6 = ["Grilled Cheese and Tomato Soup",3.00,'bread','butter','cheese','tomato soup']
rec7 = ["Chicken Parmesan",5.00,'chicken breast','parmesan cheese','pasta noodles','pesto']
rec8 = ["Fettuccine Alfredo",4.00,'fettuccine noodles','parmesan cheese','butter','heavy cream']
rec9 = ["Salmon Skillet",6.00,'salmon filet', 'cherry tomatos', 'sugar snap peas','lime', 'olive oil']
rec10 = ["Hamburger Macaroni",3.00,'ground beef','macaroni','onion','tomato','chili pepper flakes']

#list of recipe
recipes = [rec1,rec2,rec3,rec4,rec5,rec6,rec7,rec8,rec9,rec10]


#user info
user_budget = []#int(input('What is you budget for the week? '))
user_servings = []#int(input('How many people are you feeding? '))


#print all the recipe available
#print('choose from the available recipes')
#for list in recipes:
    #print(list[0])

#set up peramiters
meal = ""
meal_cost = 0
total_cost = 0
grocery_list = [] #<----figure out how to remove duplicates and add multiples


### this is the form
@app.route('/')
def userform():
   return render_template('userform.html',recipes=recipes,user_budget=user_budget, user_servings=user_servings) #tells which var to pass to html

### this is the next page with grocery list and budget info
@app.route('/result',methods = ['POST','GET'])
def budget_pie():
    if request.method == 'POST': #when submit button is pushed
        result = request.form #gets the user selections from te form
        #setting up variables
        total_cost = 0 
        budget_dif = 0
        user_budget = request.form['user_budget'] #from form selections
        user_servings = request.form['user_servings'] #from form selections
        mon_meal = request.form['mon_meal'] #from form selection
        mon_bud = 0
        tue_meal = request.form['tue_meal'] 
        tue_bud = 0
        wed_meal = request.form['wed_meal']
        wed_bud = 0
        thu_meal = request.form['thu_meal']
        thu_bud = 0
        fri_meal = request.form['fri_meal']
        fri_bud = 0
        sat_meal = request.form['sat_meal']
        sat_bud = 0
        sun_meal = request.form['sun_meal']
        sun_bud = 0

        for list in recipes: #iterate thru recipes
            if mon_meal == list[0]: #when recipe name matches mon selection 
                total_cost += list[1] * float(user_servings) #multiply the servings but the cost per serving in rec list. add to total
                mon_bud = list[1] * float(user_servings) #aggrigate cost up to today
            
            else:
                pass
            if tue_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                tue_bud = mon_bud + list[1] * float(user_servings )
            else:
                pass
            
            if wed_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                wed_bud = tue_bud + list[1] * float(user_servings )
            else:
                pass

            if thu_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                thu_bud = wed_bud + list[1] * float(user_servings )
            else:
                pass

            if fri_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                fri_bud = thu_bud + list[1] * float(user_servings )
            else:
                pass

            if sat_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                sat_bud = fri_bud + list[1] * float(user_servings )
            else:
                pass

            if sun_meal == list[0]:
                total_cost += list[1] * float(user_servings)
                sun_bud = sat_bud + list[1] * float(user_servings )
            else:
                pass

            if total_cost > float(user_budget): #if the the total cost is higher than the budget
                msg = "Selections are over budget by $"+ str(total_cost-float(user_budget)) + '0 !'
            else:
                msg = " You are under budget by $" + str(float(user_budget) - total_cost) +'0 !'

        total_deg = total_cost*(360/float(user_budget)) #this feeds the budget pie chart. Figures how many dollars for each degree of the chart so that 100% budget is 100% of chart area. 
    return render_template("result.html", mon_bud=mon_bud, tue_bud=tue_bud,wed_bud=wed_bud, 
    thu_bud=thu_bud,fri_bud=fri_bud,sat_bud=sat_bud,sun_bud=sun_bud,total_cost=total_cost,
    result=result, recipes=recipes, total_deg=total_deg, msg = msg,) #says do the calculations and send the following info to the result file

if __name__ == '__main__': #runs the app
   app.run(debug = True)
