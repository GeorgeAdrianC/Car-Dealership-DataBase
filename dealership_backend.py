import sqlite3

# creates the database:
def connect():
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()
    #creating the database table:
    cursor_.execute("CREATE TABLE IF NOT EXISTS dealership (id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER, km INTEGER, fuel TEXT, vin TEXT, color TEXT, price REAL)")
    connect_.commit()
    connect_.close()

# creates function that inserts data to the database 
def insert(make, model, year, km, fuel, vin, color, price):
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()
    cursor_.execute("INSERT INTO dealership VALUES(NULL,?,?,?,?,?,?,?,?)",(make, model, year, km, fuel, vin, color, price))
    connect_.commit()
    connect_.close()

# creates function that fetches all the data 
def view():
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()
    cursor_.execute("SELECT * FROM dealership") # -> select all from db
    rows = cursor_.fetchall() # -> returns the data and stores it in rows variable
    connect_.close()
    return rows

# creates search function, user can search by any parameter 
def search(make="", model="", year="", km="", fuel="", vin="", color="", price=""): # parameter="" in case user searches for only one parameter
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()
    cursor_.execute(
        "SELECT * FROM dealership WHERE make=? OR model=? OR year=? OR km=? OR fuel=? OR vin=? OR color=? OR price=?",
        (make, model, year, km, fuel, vin, color, price)
        ) 
    rows = cursor_.fetchall() 
    connect_.close()
    return rows

# creates the delete function, deletion by id
def delete(id):
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()                 
    cursor_.execute("DELETE FROM dealership WHERE id=?",(id,))
    connect_.commit()
    connect_.close()

# creates update function    
def update(id,make, model, year, km, fuel, vin, color, price):
    connect_ = sqlite3.connect("dealership.db")
    cursor_ = connect_.cursor()                 
    cursor_.execute(
        "UPDATE dealership SET make=?, model=?, year=?, km=?, fuel=?, vin=?, color=?, price=? WHERE id=?",
        (make, model, year, km, fuel, vin, color, price, id)
        )
    connect_.commit()
    connect_.close()
    
    

