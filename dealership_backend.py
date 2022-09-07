import sqlite3


class Database:
    
    # creates the database:
    def __init__(self,db):
        self.connect_ = sqlite3.connect(db)
        self.cursor_= self.connect_.cursor()
        #creating the database table:
        self.cursor_.execute("CREATE TABLE IF NOT EXISTS dealership (id INTEGER PRIMARY KEY, make TEXT, model TEXT, year INTEGER, km INTEGER, fuel TEXT, vin TEXT, color TEXT, price REAL)")
        self.connect_.commit()
 

    # creates function that inserts data to the database 
    def insert(self, make, model, year, km, fuel, vin, color, price):  
        self.cursor_.execute("INSERT INTO dealership VALUES(NULL,?,?,?,?,?,?,?,?)",(make, model, year, km, fuel, vin, color, price))
        self.connect_.commit()
        

    # creates function that fetches all the data 
    def view(self):  
        self.cursor_.execute("SELECT * FROM dealership") # -> select all from db
        rows = self.cursor_.fetchall() # -> returns the data and stores it in rows variable        
        return rows

    # creates search function, user can search by any parameter 
    def search(self, make="", model="", year="", km="", fuel="", vin="", color="", price=""): # parameter="" in case user searches for only one parameter  
        self.cursor_.execute(
            "SELECT * FROM dealership WHERE make=? OR model=? OR year=? OR km=? OR fuel=? OR vin=? OR color=? OR price=?",
            (make, model, year, km, fuel, vin, color, price)
            ) 
        rows = self.cursor_.fetchall()         
        return rows

    # creates the delete function, deletion by id
    def delete(self, id):                   
        self.cursor_.execute("DELETE FROM dealership WHERE id=?",(id,))
        self.connect_.commit()
        

    # creates update function    
    def update(self, id, make, model, year, km, fuel, vin, color, price):                   
        self.cursor_.execute(
            "UPDATE dealership SET make=?, model=?, year=?, km=?, fuel=?, vin=?, color=?, price=? WHERE id=?",
            (make, model, year, km, fuel, vin, color, price, id)
            )
    
    def __del__(self):
        self.connect_.close()
