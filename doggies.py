# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:36:34 2016

@author: ian.weinstock
"""
from __future__ import print_function
from twilio.rest import TwilioRestClient
accountSID = 'ACfc1b30388c2f334ac2438016f5b56655'
authToken = '00f079567e035cbb02a823f93412a870'
import urllib2


response = urllib2.urlopen('http://www.petharbor.com/results.asp?searchtype=LOST&start=3&friends=1&samaritans=1&nosuccess=0&orderby=Brought%20to%20the%20Shelter&rows=1000&imght=120&imgres=thumb&tWidth=200&view=sysadm.v_pgeo&bgcolor=ffffff&text=000000&link=000080&alink=800000&vlink=000080&fontface=arial&fontsize=10&col_hdr_bg=cbd6ea&col_hdr_fg=000080&col_bg=3568B5&col_bg2=DAE1EB&SBG=CBD6EA&miles=20&shelterlist=%27PGEO%27&atype=&where=type_DOG&NewOrderBy=Brought%20to%20the%20Shelter&PAGE=1')
html = response.read()
doggies = ['Poodle','Shih Tzu','Havanese','Bichon Frise','Lhasa Apso', 'Tibetan', 'Pit Bull']
shelter_dogs = []
for dog in doggies:
    if dog in html:
        shelter_dogs.append(dog)   
if len(shelter_dogs) == 0:
    print("No dogs yet")
elif len(shelter_dogs) == 1:
    print(shelter_dogs[0])
elif len(shelter_dogs) == 2:
    shelter_dogs.insert(len(shelter_dogs)-1,'and')
    shelter_dogs.append(" http://bit.ly/29qnqca")
    for dogs in shelter_dogs:
        print(dogs,sep="", end=" ")
    print('http://bit.ly/29qnqca')
else:
    shelter_dogs.insert(len(shelter_dogs)-1,'and')
    shelter_dogs.append(" http://bit.ly/29qnqca")
    for dogs in shelter_dogs:
        print(dogs,sep=",", end=" ")
    print('http://bit.ly/29qnqca')
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14434064411'
myCellPhone = '+14434660091'
message = twilioCli.messages.create(body=shelter_dogs, from_=myTwilioNumber, to=myCellPhone)
