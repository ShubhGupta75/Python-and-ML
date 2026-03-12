# Building Url Dynamically
# Variable Rule
# Jinja 2 Template Engine

'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
  return "<html><h1>Welcome to the flask course</h1></html>"

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Variable Rule
@app.route('/success/<int:score>') # '/base url/ url variable'
def success(score):
   res=''
   if score>50:
      res='PASS'
   else:
      res='FAIL'
   return render_template('result.html', results=res)
   # Loads result.html from the 'templates/' folder, Sends a variable 'results = res' to HTML, Inside 'result.html', you can access it.

# Using for loop in Jinja 2 Template Engine
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,"res":res} # passing key,value pairs as a variable.

    return render_template('result1.html',results=exp)

# Using conditional statement in Jinja 2 Template Engine
@app.route('/successif/<int:score>')
def succesif(score):
   return render_template('result.html',results=score)


@app.route('/fail/<int:score>')
def fail(score):
   return render_template('result.html',results=score)


# Redirect and url_for
@app.route('/submit', methods=['GET','POST'])
def submit():
   total_score=0
   if request.method=='POST':  # Handling POST Request
      science=float(request.form['science'])
      maths=float(request.form['maths'])
      c=float(request.form['c'])
      data_science=float(request.form['datascience'])

      total_score=(maths+science+c+data_science)/4
   else:
      return render_template('submit.html')  # Handling GET Request
   return redirect(url_for('successres', score=total_score)) # Redirecting to Another Route

# url_for() is used for building dynamic URL.
# Calls route function named 'successres' => Passes 'score' as URL parameter


if __name__ == '__main__':
  app.run(debug = True)
