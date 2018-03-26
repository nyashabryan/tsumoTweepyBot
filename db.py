import sqlite3
import sys

db_name = "info.db"
init_src = "tsumo.txt"
new_tsumo = "new_tsumo.txt"
keys_src = "keys"

def create_tables():
    tsumo_lines = []
    keys_lines = [] 
    with open(init_src, "r") as f:
        tsumo_lines = f.readlines()

    with open(keys_src, "r") as f:
        keys_lines =  f.readlines()


    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #Create the Tsumo table and poulate it with Tsumos

    c.execute('''CREATE table Tsumo 
                (ID integer primary key, tsumo text, meaning text)''')

    for line in tsumo_lines:
        c.execute('''INSERT INTO Tsumo(tsumo) values (?)''',(line[:-1],))

    #Create the keys table and populate it with Keys
    
    c.execute('''CREATE TABLE Keys
                (key text, value text)''')

    for line in keys_lines:
        if len(line) == 0:
            continue
        c.execute('''INSERT INTO Keys (key, value) values (?, ?)''', (line.split(": ")[0], line.split(": ")[1][:-1]))
        
    
    conn.commit()
    conn.close()

def get_tsumo(x):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('''SELECT tsumo FROM Tsumo WHERE ID = ?''', (x,))
    result = c.fetchone()
    conn.close()
    return str(result[0])

def get_tsumo_count():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''SELECT count(*) FROM Tsumo''')
    result = c.fetchone()
    return int(result[0])

def new_tsumo():
    new_lines = []
    new_tsumo = []
    with open(new_tsumo, "r") as f: 
        new_lines = f.readlines()

    for line in new_lines:
        new_tsumo.append(new_lines[:-1])

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    x = c.rowcount
    for tsumo in new_tsumo:
        c.execute('''INSERT INTO Tsumo(tsumo) 
                SELECT ? 
                FROM dual
                WHERE NOT EXISTS( SELECT 1
                FROM FUNDS
                WHERE tsumo ==  ?)''', tsumo)
    y = c.rowcount

    if x ==y:
        print ("No new rows were added.")

    else:
        print(y-x, " rows were added.")

    with open(new_tsumo, "w") as f:
        f.write("")

def get_keys():
    
    keys = {}
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    c.execute('''SELECT key, value  FROM Keys''')
    results = c.fetchall()
    for result in results: 
        keys[result[0]] =  result[1]

    conn.commit()
    conn.close()

    return keys


def delete_table():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('''DROP TABLE Tsumo''')
    conn.commit()
    conn.close()

# Running db methods

if __name__ == "__main__":
    args =  str(sys.argv)[1:]
    
    if args[0] == "create_tables":
        create_tables()

    elif args[1] ==  "new_tsumo":
        new_tsumo()

    elif args[1] == "delete_table":
        delete_table()
    else:
        pass




