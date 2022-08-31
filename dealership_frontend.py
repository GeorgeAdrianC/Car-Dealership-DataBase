from tkinter import *
from turtle import width
import dealership_backend


"""
A program that stores a car dealership database,
it manages all entries, editing and exists of cars.

Information of cars in the data base:
Make, Model
Year, Km
Fuel Type, VIN
Color, Price.

User can: 
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

# function is binded to the delete widget event 
def get_selected_row(event):
                    # ^ special parameter that holds the information about the type of the event
    global selected_tuple
    index = list_box.curselection()[0] # -> gets the index of the row 
    selected_tuple = list_box.get(index) # -> gets the selected tuple
    #shows the selected row values in their widgets:
    make_e.delete(0,END)
    make_e.insert(END, selected_tuple[1])
    model_e.delete(0,END)
    model_e.insert(END, selected_tuple[2])
    year_e.delete(0,END)
    year_e.insert(END, selected_tuple[3])
    km_e.delete(0,END)
    km_e.insert(END, selected_tuple[4])
    fuel_e.delete(0,END)
    fuel_e.insert(END, selected_tuple[5])
    vin_e.delete(0,END)
    vin_e.insert(END, selected_tuple[6])
    color_e.delete(0,END)
    color_e.insert(END, selected_tuple[7])
    price_e.delete(0,END)
    price_e.insert(END, selected_tuple[8])

# connects view function to the button
def view_command():
    list_box.delete(0, END) # -> we make sure that when the db is executed the list box is empty
    for row in dealership_backend.view():
        list_box.insert(END,row) # -> the new rows will be put at the end of the list
    
# connects search function to the button
def search_command():
    list_box.delete(0, END)
    for row in dealership_backend.search(
        make_value.get().upper(),model_value.get(),year_value.get(),km_value.get(),
        fuel_value.get(),vin_value.get(),color_value.get(),price_value.get()
        ):
        list_box.insert(END,row)

# connects insert function to the button
def insert_command():
    dealership_backend.insert(
        make_value.get().upper(),model_value.get().upper(),year_value.get(),km_value.get(),
        fuel_value.get().upper(),vin_value.get().upper(),color_value.get().upper(),price_value.get()
        )
    list_box.delete(0, END)
    list_box.insert(END,
        (make_value.get().upper(),model_value.get().upper(),year_value.get(),km_value.get(),
        fuel_value.get().upper(),vin_value.get().upper(),color_value.get().upper(),price_value.get()
        ))

# connects delete function to the button
def delete_command():
    dealership_backend.delete(selected_tuple[0]) # -> we get the index number of the selected row tot delete it

# connects the update function to the button
def update_command():
    #updates the selected widget
    dealership_backend.update( 
        selected_tuple[0],make_value.get().upper(),model_value.get().upper(),year_value.get(),km_value.get(),
        fuel_value.get().upper(),vin_value.get().upper(),color_value.get().upper(),price_value.get()
        ) 

# connects the clear function to the button
def clear_widgets():
    make_e.delete(0,END)   
    model_e.delete(0,END)  
    year_e.delete(0,END)   
    km_e.delete(0,END)   
    fuel_e.delete(0,END)  
    vin_e.delete(0,END)   
    color_e.delete(0,END)   
    price_e.delete(0,END)

    
# opening the window object with the tkinter(Tk) method
window=Tk()

photo_icon = PhotoImage(file = "car-icon.png")
window.iconphoto(False, photo_icon)

# adding title to the window
window.wm_title("Car Dealership DataBase")

# creating the labels 
make_l = Label(window,text="Make")
make_l.grid(row=1,column=1) # -> griding the widget

# and the entry for each label
make_value=StringVar()  # -> the function that creates the special object    
make_e = Entry(window,textvariable=make_value,width=30) # -> the text variable parameter expects
make_e.grid(row=1,column=2)                             #    a value that the user will input in the entry widget(special data type StringVar())

model_l = Label(window,text="Model")
model_l.grid(row=1,column=3)

model_value=StringVar()
model_e = Entry(window,textvariable=model_value,width=39)
model_e.grid(row=1,column=4,columnspan = 3)

year_l = Label(window,text="Year")
year_l.grid(row=2,column=1)

year_value=StringVar()
year_e = Entry(window,textvariable=year_value,width=30)
year_e.grid(row=2,column=2)

km_l = Label(window,text="Km")
km_l.grid(row=2,column=3)

km_value=StringVar()
km_e = Entry(window,textvariable=km_value,width=39)
km_e.grid(row=2,column=4,columnspan = 3)

fuel_l = Label(window,text="Fuel Type")
fuel_l.grid(row=3,column=1)

fuel_value=StringVar()
fuel_e = Entry(window,textvariable=fuel_value,width=30)
fuel_e.grid(row=3,column=2)

vin_l = Label(window,text="VIN")
vin_l.grid(row=3,column=3)

vin_value=StringVar()
vin_e = Entry(window,textvariable=vin_value,width=39)
vin_e.grid(row=3,column=4,columnspan = 3)

color_l = Label(window,text="Color")
color_l.grid(row=4,column=1)

color_value=StringVar()
color_e = Entry(window,textvariable=color_value,width=30)
color_e.grid(row=4,column=2)

price_l = Label(window,text="Price(€)")
price_l.grid(row=4,column=3)

price_value=StringVar()
price_e = Entry(window,textvariable=price_value,width=39)
price_e.grid(row=4,column=4,columnspan = 3)

#setting up the list box where the results where gonna be printed
list_box = Listbox(window, height =9, width=60)
list_box.grid(row=5,column=1, rowspan=7,columnspan = 4)

#setting up the scroll bar for the list box
scroll_bar = Scrollbar(window)
scroll_bar.grid(row=5, column=5, rowspan=7)

list_box.configure(yscrollcommand=scroll_bar.set, height=18) # -> the vertical scrollbar along the y axis it will be set to the scroll_bar
scroll_bar.configure(command=list_box.yview) # -> command that when we scroll the bar the vertical view would change 

#we bind the delete function to the list_box
list_box.bind("<<ListboxSelect>>", get_selected_row)
           # event type ^          ^ function that returns a tuple object with the selection, py expects the event parameter from the function

#setting up the buttons for the commands
view_e = Button(window,text="View All",width=15,command=view_command)
view_e.grid(row=5,column=6)

search_e = Button(window,text="Search Entry",width=15, command=search_command)
search_e.grid(row=6,column=6)

insert_e = Button(window,text="Add Entry",width=15, command=insert_command)
insert_e.grid(row=7,column=6)

update_e = Button(window,text="Update Selected",width=15, command=update_command)
update_e.grid(row=8,column=6)

delete_e = Button(window,text="Delete Selected",width=15, command=delete_command)
delete_e.grid(row=9,column=6)

clear_e = Button(window,text="Clear Widget Spaces",width=15, command= clear_widgets)
clear_e.grid(row=10,column=6)

close_e = Button(window,text="Close",width=15, command= window.destroy)
close_e.grid(row=11,column=6)








#ending with the main loop method so the window remains open
window.mainloop()
    