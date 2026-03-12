# Basic skeleton of a flask app

from flask import Flask

'''
 It creates an instance of the Flask class, which will be our WSGI (Web Server Gateway Interface) application.
'''

# WSGI application
app = Flask(__name__) # initializing the flask

# Basic route
@app.route('/') # this decorator is pointing towards the 'welcome' function, that means when '/' is entered, it will execute the 'welcome' function.
def welcome():
  return "Welcome to my flask website. Hope i complete my ML before my birthday"


@app.route('/index')
def index():
  return "Welcome to the index page"

if __name__ == '__main__':
  app.run(debug = True)  # this will restart the server whenever any changes is made.
