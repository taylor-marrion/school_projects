# Flask_HTML2.py
# Author: Taylor Marrion
# Date: 2/29/2020
"""This application generates a HTML page for a web application."""

from flask import Flask
from flask import request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/Lab7')

def helloIndex():
    myReply = popHead();
    myReply += popH1("Welcome to Taylor's Super Fancy Web App!")
    
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    myReply += (f"<p>You accessed this web app at: {date_time} </p>") # Enter Date and Time
    
    myReply += popH3("This is the header before I show you some lists.")
    myReply += popH4("Now it's time for an ordered list.")
    myReply += popOL()
    myReply += popH4("This page has it all folks, even an UNordered list.")
    myReply += popUL()
    myReply += popH3("Here is a table with some data from different states.")
    myReply += popTable()
    myReply += popH3("Please enter your name into the vistor log!")
    myReply += popForm()
    myReply += popH3("Another header. This time, I give you links to click.")
    myReply += popComment("Author of this site holds no ownership of content of the following links.")
    myReply += popPara("There's a comment here, but you can't see it. I'm very sneaky.")
    myReply += popLink("A programmer's best friend","https://stackoverflow.com/")
    myReply += popLink("Where we go when our best friend fails us","https://www.google.com")
    myReply += popLink("And here's a dog just trying his best","https://www.youtube.com/watch?v=ND63UPelkIw")
    myReply += popFoot()
    myReply += popEnd()
    return myReply

def popHead():
    headData = "<!DOCTYPE html> "
    headData +="<head> "
    headData +="<title>Taylor's web app</title>"
    headData +="</head>"
    headData +="<body>"
    return headData

def popH1(myString):
    newString = '<H1>' + myString + '</H1>'
    return newString

def popH2(myString):
    newString = '<H2>' + myString + '</H2>'
    return newString

def popH3(myString):
    newString = '<H3>' + myString + '</H3>'
    return newString

def popH4(myString):
    newString = '<H4>' + myString + '</H4>'
    return newString

def popPara(myString):
    newString = "<p>"
    newString += myString
    newString += "</p>"
    return newString

def popOL():
    newString = "<ol>"
    newString += "<li> Ben & Jerry's </li>"
    newString += "<li> Haagen-Dazs </li>"
    newString += "<li> Breyer's </li>"
    newString += "<li> Blue Bell </li>"
    newString += "</ol>"
    return newString

def popUL():
    newString = "<ul>"
    newString += "<li> 2001: A Space Odyssey </li>"
    newString += "<li> A Clockwork Orange </li>"
    newString += "<li> The Shining </li>"
    newString += "<li> Full Metal Jacket </li>"
    newString += "</ul>"
    return newString

def popTable():
    newString = "<table padding='30' border='1'>"
    newString += "<caption> States Data. Getting fancier, right? </caption>"
    newString += "<tr style='text-align: center; vertical-align: middle;'>"
    newString += "<th> State </th>"
    newString += "<th> Bird </th>"
    newString += "<th> Flower </th>"
    newString += "</tr>"
    newString += popRow(["Hawaii","HawaiiFlag.png","Nene","Hibiscus"])
    newString += popRow(["Montana","MontanaFlag.png","Western Meadowlark","Bitterroot"])
    newString += popRow(["Ohio","OhioFlag.png","Cardinal","Scarlet Carnation"])
    newString += popRow(["Virginia","VirginiaFlag.png","Cardinal","Dogwood"])
    newString += "</table>"
    return newString

def popRow(myList):
    state = myList[0]
    flag = myList[1]
    bird = myList[2]
    flower = myList[3]
    newString = "<tr style='text-align: center; vertical-align: middle;'>"
    newString += "<td> <figure>"
    newString += f"<img src='static/{flag}' alt='{state}' >"
    newString += f"<figcaption> {state} </figcaption>"
    newString += "</figure> </td>"
    newString += f"<td> {bird} </td>"
    newString += f"<td> {flower} </td>"
    newString += "</tr>"
    return newString

def popForm():
    newString = "<form action='/visitorLog' method='post'>"
    newString += "<label for='vistor'> Name: </label> <input type='text' name='vistor'>"
    newString += "<label for='state'> State: </label> <input type='text' name='state'>"
    newString += "<br/>"
    newString += "<label for='feedback' style='display: block;'> Please provide feedback on your experience: </label>"
    newString += "<textarea name='feedback' rows = '5' cols='40'> </textarea>"
    newString += "<br/>"
    newString += "<label for='selection'> Would you like to see more states? </label>"
    newString += "<select id='selection'>"
    newString += "<option> Too bad </option>"
    newString += "<option> So sad </option>"
    newString += "<option> That is all you get </option>"
    newString += "</select>"
    newString += ""
    newString += ""
    newString += "<br/>"
    newString += "<input type='submit' class='submit' value='Submit'>"
    newString += "<input type='reset' value='Reset'>"
    newString += "</form>"
    return newString

def popComment(myString):
    newString = "<!-- "
    newString += myString
    newString += " -->"
    return newString

def popLink(myString,url):
    newString = f'<p><a href="{url}">{myString}</a></p>'
    return newString
    
def popFoot():
    newString = "<div>"
    newString += "<hr/>"
    newString += '<p style="font-size:65%;">'
    newString += "Created by Taylor Marrion. Thanks for stopping by!"
    newString += "</p>"
    newString += '<p style="font-size:65%;">'
    newString += "This was going to be a sticky footer that stayed at the bottom of the page, but it started to clutter up my code."
    newString += "</p>"
    return newString

def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData

@app.route('/visitorLog',methods=['POST'])
def visitorLog():
    return True

app.run(host='0.0.0.0', port= 8080)