#!/usr/bin/env python3

# print ("If you have not done this already; you need to install guizero with pip install guizero")

# import used stuff and set window details

from guizero import App, Text, TextBox, PushButton

app = App(title="Hello world", layout="grid", width=300, height=110)

# app wide variables (unused for now)

# definitions of functions go below

responsetextvar = ("test")

def say_back():
  if userresponse.value == "hello":
    responsetext.value = ("Well done!")
  else :
    responsetext.value = ("Not quite the instruction.")

def reset_text():
  responsetext.value = ("")

# gui creation below

header = Text(app, text="Hello GitHub! Now say hello.", grid=[0,0])
userresponse = TextBox(app, width="fill", grid=[0,1])
userresponse.focus()
resetbutton = PushButton(app, text="reset", grid=[2,1], command=reset_text)
userresponsebutton = PushButton(app, text="say", grid=[1,1], command=say_back)
responsetext = Text(app, text="", grid=[0,2,2,2])

app.display()