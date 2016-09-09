#!/usr/bin/python3.5

import sys
import shutil
import os
import pickle
import collections #OrderedDict

user = {"economy": 9001, # It's over 9000!
        "planetNum": 1,
        "planetID": ["1"],
       "fleetNum": 1,
        "fleetID": ["1"],
        }

fleets = {"1" : {"ships": 100000},
         } 


# planet table
# 
# ID City Education
#
#

planet = {"1" : {"city": 1,       # city ->  capital -> Metropolies 
                "education": 1},  # University Levels}
        }


def grabPlanetObj(user, planet, pid=[]):
    """ 
    Grab planets from user id
    """

    planet_id = [x for x in user["planetID"]] 
    plist = []
    for i in planet_id:
        plist.append(planet[i])
    
    return plist

def grabFleetObj(user, fleet, pid=[]):
    """
    Grab fleet from user id
    """

    fleet_id = [ x for x in user["fleetID"]]
    flist = []
    for i in fleet_id:
        flist.append(fleet[i])

    return flist


def show_user(user):
    os.system("clear")
    
    userSorted = collections.OrderedDict(sorted(user.items()))
    for obj in userSorted:
        print(obj, ": " , user[obj])

    print("\n")
    print(grabPlanetObj(user, planet))
    pause = input("Paused")

def add_option(members):
    os.system("clear")
    name = input("Please enter name: ")
    code = input("Please enter optiono: ")
    members[name] = code
    with open('filename.pickle', 'wb') as handles:
        pickle.dump(members, handles)
        print("saved")
        


try:
    with open('filename.pickle', 'rb') as handles:
        members = pickle.load(handles)
        #show_members(members)
except:
    print("There may be a problem with file")
    pause = input("paused")
    members = {}

def show_menu():
    os.system("clear")
    print("\n","*" * 12, "MENU", "*" * 12)
    print("1. List options")
    print("2. Add option")
    print("3. Delete option")
    print("99. Save")
    print("0. Abort")
    print("*" * 28, "\n")
    return input("Please make a selection: ")

while True:
    ret = show_menu()
    if ret  == "1":
        show_user(user)
    elif ret == "2":
        add_option(members)
    else:
        print("No Values")
        break