#******************************************************
#testing to run the UI thrugh flask
from flask import Flask, render_template, request
app = Flask(__name__)
### this is the form
@app.route('/')
def student():
   return render_template('student.html')

### this is the table on the next page
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)