from flask import render_template
import random
from helloapp import app, db
from helloapp.models import Quotes


## Define below a view function 'hello', which displays the message
## "Hello World!!! I've run my first Flask application."
## The view function 'hello' should be mapped to URL '/' .
## The view function must render the template 'index.html'

@app.route('/')
def home():
    return render_template('index.html')

def addToDb():

        quote1 = Quotes(quotestring="Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.",
                        quoteauthor='Albert Einstein')

        quote2 = Quotes(quoteauthor='Abraham Lincoln',
                        quotestring="Give me six hours to chop down a tree and I will spend the first four sharpening the axe.")

        quote3 = Quotes(quoteauthor='Benjamin Franklin',
                        quotestring="Tell me and I forget. Teach me and I remember. Involve me and I learn.")

        quote4 = Quotes(quoteauthor='Willian Shakespeare',
                        quotestring="Listen to many, speak to a few.")

        quote5 = Quotes(quoteauthor='Warren Buffett',
                        quotestring="Only when the tide goes out do you discover who's been swimming naked.")

        db.session.add(quote1)
        db.session.add(quote2)
        db.session.add(quote3)
        db.session.add(quote4)
        db.session.add(quote5)

        db.session.commit()



def deleteFromDb():

     quotes = Quotes.query.all()
     for i in quotes:
        db.session.delete(i)
        db.session.commit()


## Define below a view function 'hello_user', which takes 'username' as an argument
## and returns the html string containing a 'h2' header  "Hello <username>"
## After displaying the hello message, the html string must also display one quote,
## randomly chosen from the provided list `quotes`
## Before displaying the quote, the html string must contain the 'h3' header 'Quote of the Day for You'
## The view function 'hello_user' should be mapped to URL '/hello/<username>/' .
## The view function must render the template 'hello_user.html'
## Use the below list 'quotes' in 'hello_user'  function
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who's been swimming naked."
##    ]
@app.route('/hello/<string:username>/')
def hello_user1(username):

    addToDb()
    quotes = Quotes.query.all()
    quotes = [ quote.quotestring for quote in quotes]
    random_quote = random.choice(quotes)
    return render_template('hello_user.html', username=username, quote=random_quote)


## Define below a view function 'display_quotes', which returns an html string
## that displays all the quotes present in 'quotes' list in a unordered list.
## Before displaying 'quotes' as an unordered list, the html string must also include a 'h1' header "Famous Quotes".
## The view function 'display_quotes' should be mapped to URL '/quotes/' .
## The view function must render the template 'quotes.html'
## Use the below list 'quotes' in 'display_quotes'  function
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who's been swimming naked."
##    ]
@app.route('/quotes/')
def display_quotes():


    quotes = [
                "Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Only when the tide goes out do you discover who's been swimming naked."
    ]
    #deleteFromDb()
    #addToDb()
    #quotes = Quotes.query.all()
    #quotes = [ quote.quotestring for quote in quotes]
    return render_template('quotes.html', quotes=quotes)

if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.

    app.run()



'''
(projenv) $ flask db env

Creating directory ....

.....

(projenv) $ flask db migrate -m "Creating user table"

....

....

Generating .../4c1a9e3a41e0_creating_user_table.py ... done

(projenv) $ flask db upgrade

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.

INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

INFO  [alembic.runtime.migration] Running upgrade  -> 4c1a9e3a41e0, Creating user table

(projenv) $ flask shell

Python ...

App: ...

Instance: ...

>>>

>>> from helloapp.models import User

>>> user1 = User(fname="James", lname="smith", email="james@abc.com")

>>> user2 = User(fname="Sam", lname="Billings", email="sam@xyz.com")


>>> from helloapp import db

>>> db.session.add(user1)

>>> db.session.add(user2)

>>> db.session.commit()

>>> User.query.all()

[<User : James smith>, <User : Sam Billings>]

>>> User.query.filter(User.fname == 'James').all()

[<User : James smith>]

'''






























