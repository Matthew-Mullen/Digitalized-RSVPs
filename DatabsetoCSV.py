#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get data from firebase put it in csv file to be read in excel
import pyrebase, os, csv

fb = pyrebase.initialize_app({
    'apiKey': os.environ['RSVP_FIREBASE_KEY'],
    'authDomain': 'rsvp-c3541.firebaseapp.com',
    'databaseURL': 'https://rsvp-c3541.firebaseio.com',
    'storageBucket': 'rsvp-c3541.appspot.com'
})
# get data from rsvplist section of database
rsvpdata=fb.database().child('rsvplist').get()
# write a row in new csv file containing guest name and how many guests each guest is bringing
with open('rsvp.csv','w',newline='') as csvfile:
    writer=csv.writer()
    for response in rsvplist.each():
        key=rsvp.key()
        for invitee in rsvp.val():
            writer.writerow([key,guest['name'],guest['numguest']])

