"""task 16 was created by Rebecca """
import sqlite3
import time
import datetime


try:
    connection = sqlite3.connect("Assignment.db")
except Exception as e:
    print(e)
else:
    print("Opened database successfully")
finally:
    print("Finishing connecting to database")

cursor = connection.cursor()


def create_table():
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS classDiagramInfo('
                   'unit REAL, className TEXT, dataNameOne TEXT, dataNameTwo TEXT, AttrName TEXT, methodName TEXT, '
                   'datetime TEXT )')
    except Exception as e:
        print(e)
        print('there is an error creating the table')
    else:
        print('table is created')

def data_entry():
    try:
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
        cursor.execute("INSERT INTO classDiagramInfo Values(1, 'Toy', 'name', 'color', 'getAttr', 'getMethod',"
                       " '2019-03-81')")
        cursor.execute("INSERT INTO classDiagramInfo Values(2, 'ToyBox', 'name', '-', 'getAttr', 'getMethod', "
                       "'2018-03-81')")
        connection.commit()
        #cursor.close()
        #connection.close()
    except Exception as e:
        print(e)
        print('there is an error inserting data into the table')
    else:
        print('there is data in the program')

def read_from_db():
    cursor.execute("SELECT * from classDiagramInfo ")
    #data = c.fetchall()
    #print(data)
    for row in cursor.fetchall():
        print(row)



#create_table()
#data_entry()
#read_from_db()
#cursor.close()
#connection.close()

