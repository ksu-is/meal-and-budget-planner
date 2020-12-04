#testing to run the UI thrugh flask
from flask import Flask, render_template, request
app = Flask(__name__)

#recipe dictionary <------ THIS WORKS!!!!
# this is a dictionary of dictionaries! Like a recipe is a cook book and each rec# is a recipie
  # rec# key is: recipe name, cost per serving, and ingredients list
recipe = {
  "rec1" : {
    "name" : "chicken",
    "cost" : 2.50,
    "ing"  : ['chicken','herbs']
  },
  "rec2" : {
    "name" : "pasta",
    "cost" : 2.50,
    "ing"  : ['pasta','sauce']
  }
}
#print(recipe)

#testing another dic set-up

#cook_book= dict.fromkeys(["name", "cost", "ing"]) #creates blank dict with keys
#print(cook_book)

#def add_recipe ():
  #cook_book["name"]=input("rec name")
  #cook_book["cost"]=input("cost per serving")
  #ingredients=input("ingredients")
  #cook_book["ing"]=ingredients

#add_recipe()
#print(cook_book)
  #try: 
    #my_list = [] 
    #user_input =  input("ingredient or q to quit")
    #while user_input!= "q": 
        #my_list.append(user_input) 
          
# if the input is not q, just print the list 
    #except: 
        #print(my_list) 
        

#add_recipe("recipe")
#print(cook_book)



#iterates thru each rec# dictionary and prints the values
for k, v in recipe.items(): 
    print(k, '=>', v) 

#NOT WORKING
#iterates thru each rec# dictionary and prints only the recipie name
for k, v in recipe.items(): 
    #print(recipe.name) 

#FOLLOWING CODE IS FOR FLASK

### this is the form
@app.route('/')
def userform():
   return render_template('userform.html')

### this is the table on the next page
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)