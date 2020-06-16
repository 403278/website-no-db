import pyodbc

# db = pyodbc.connect(
#     "Driver={ODBC Driver 13 for SQL Server};"
#     "Server=192.168.1.5;"
#     "Database=ihostgroup1;"
#     "UID=sa;"
#     "PWD=CrystalCastles;"
# )
db = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-80DIMLO;"
    "Database=HR2;"
    "Trusted_dbection=yes;"
)

c = db.cursor()

def readCreds(username):
    with db:
        c.execute("SELECT * FROM myCred WHERE username = ?",(username,))
        return c.fetchone()

def registerNewCreds(username, password, email):
    with db:
        c.execute("INSERT INTO myCred VALUES (?, ?, ?);",
        (username, password, email)
        )

def insertItemIntoInventory(itemName, model, category, condition, description):
    with db:
        c.execute(
            "INSERT INTO Inventory VALUES (?, ?, ?, ?, ?);",
            (itemName, model, category, condition, description)
        )

def readItemsFromTable(table):
    with db:
        c.execute("SELECT * FROM ?",(table,))

def checkUser(username):
    with db:
        c.execute("SELECT username FROM myCred WHERE username = ?",(username,))
        return c.fetchone()



# def deleteItemFromTable():        #TO-DO IF NEEDED
#     with db:
#         c.execute("DELETE FROM Inventory WHERE")