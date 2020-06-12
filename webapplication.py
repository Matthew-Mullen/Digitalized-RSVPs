#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Server for receiving user input into database (RSVP)
import os
import pyrebase
from flask import Flask, request, render_template, redirect
# create an instance of the flask class
app=Flask(__name__,static_url_path='')

# create and initialize firebase application instance
firebase = pyrebase.initialize_app({
    'apiKey': os.environ['RSVP_FIREBASE_KEY'],
    'authDomain': 'rsvp-c3541.firebaseapp.com',
    'databaseURL': 'https://rsvp-c3541.firebaseio.com',
    'storageBucket': 'rsvp-c3541.appspot.com'
})
# get database service for RSVP app (could use argument but it is default in my firebase)
database=firebase.database()

# render the template called website.html stored in adjacent folder called template
@app_route('/')
def index():
    # go to website.html by default
    return render_template('website.html')

# receive data and push to database
@app.route('/rsvp', methods=['POST'])
def rsvp():
    # receive user input (rsvp) from the website
    data = request.get_json()
    database.child('rsvplist').push(data)
    # 204 indicates request has been completed successfully
    return ('', 204)
# if running this program as the main program the interpreter assigns the string "__main__" to the __name__ variable
if __name__=="__main__":
    app.run(debug=False)
    

