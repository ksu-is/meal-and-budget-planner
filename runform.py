#testing to run the UI thrugh flask
from flask import Flask, render_template, request
app = Flask(__name__)

#recipe dictionary <------ THIS WORKS!!!!
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
for k, v in recipe.items(): 
    print(k, '=>', v) 

for k, v in recipe.items(): 
    print(recipe.name) 

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