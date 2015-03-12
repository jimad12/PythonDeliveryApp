#!/usr/bin/python

from Tkinter import *
import tkMessageBox
#from Tkinter import messagebox as tkMessageBox

#define the save_data function for the above fields, save info to txt file
def save_data():
  try:
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" %address.get("1.0", END))
    #depot.delete(0, END)
    description.delete(0, END)
    address.delete(1.0, END)
  
  except Exception as ex:
    #Display an error in a popup window
    tkMessageBox.showerror("Error!", "Can't write to the file\n %s" % ex)    
  
def read_depots(file):
  depots = []
  depots_f=open(file)
  for line in depots_f:
    depots.append(line.rstrip())
  return depots   
     
  
app = Tk()

app.title('Head-Ex Deliveries')
#Depot field info
Label(app, text ="Depot:").pack()
#depot = Entry(app)
#depot.pack()

#In order to prevent ambiguity, using radio buttons to specify address

#create a model (MVC)
depot = StringVar()
""""
#Radio buttons option for depot locations
Radiobutton(app, variable = depot, text ="Seattle, WA", value="Seattle,WA").pack()
Radiobutton(app, variable = depot, text ="Cambridge, MA", value ="Cambridge, MA").pack()
Radiobutton(app, variable = depot, text ="Cambridge, UK", value="Cambridge, UK").pack()
Radiobutton(app, variable = depot, text ="Rotterdam, NL", value="Rotterdam, NL").pack()
"""
depot.set("Your Location")

bodyText = Label(app, text="Select The nearest Depot to your location for deliveries", height = 3)
bodyText.pack()

options = read_depots("depots.txt")# now add the new locations for the select-opton menu
OptionMenu(app, depot, *options).pack()

#description Filed info
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

#Address field info
Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

#save button
Button(app, text="Save", command = save_data).pack()
app.mainloop()