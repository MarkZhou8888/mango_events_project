import os
from app import app
from flask import render_template, request, redirect

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'events'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:UBgD2uKt2OzdVa6c@cluster0-aenak.mongodb.net/events?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connect to database
    connect = mongo.db.events
    #query the database to get all of the events
    events = list(connect.find({}))
    print(events)
    return render_template('index.html', events = events)

    #Change your (‘/index) route to display the real events from your database. Consider the following in your route.



# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    test = mongo.db.test
    # insert new data
    test.insert({'name': 'last day of school'})
    # return a message to the user
    return "Added data to database!"

@app.route('/input')

def input():
    #check our HTML file to see if form appears
    return render_template("input.html")

@app.route('/results', methods = ["Get","Post"])
def results():
    userdata = dict(request.form)
    print(userdata)
    event_name = userdata['name']
    print(event_name)
    event_date = userdata['date']
    print(event_date)
    events = mongo.db.events
    events.insert({"name": event_name, "data": event_date})

    return redirect('/index')
