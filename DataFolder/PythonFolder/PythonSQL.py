from dataclasses import dataclass
from unicodedata import name
import mysql.connector
import os


def createDB(nameDB,mycursor):
    
    sqlFormula = "SHOW DATABASES LIKE %s"
    mycursor.execute(sqlFormula, (nameDB,))
    results = mycursor.fetchone()

    if results:
        print("dataBase already created")
    else:
        sql = "CREATE DATABASE dataSummerInternship"
        mycursor.execute(sql)
        print("DataBase created")


def connection():
    mydb = mysql.connector.connect(
        host = "localhost", # change if you want an online database
        user="root",
        passwd="Thomasthomas66"   
    )
    return mydb

def createTable(nameTable, mycursor):

    stmt = "SHOW TABLES LIKE %s" # check if the table exists
    mycursor.execute(stmt, (nameTable,))
    result = mycursor.fetchone()
   
    if result:
        print("this table name already exists")
    else:
        mycursor.execute("CREATE TABLE signals (signalsID INT, signalDate VARCHAR(255), type VARCHAR(255))")



def insertInfo(nameTable, mycursor, id, signalDate, type):

    stmt = "SHOW TABLES LIKE %s" # check if the table exists
    mycursor.execute(stmt, (nameTable,))
    result = mycursor.fetchone()

    if result:
        sqlFormula = "INSERT INTO signals VALUES (%s, %s, %s)"
        mycursor.execute(sqlFormula , (id, signalDate, type))
        
    else:
        print("Sorry, this table seems to not exist...We can't insert your information")

    

def getFiles(path):
    list = os.listdir(path)
    return list


def main():
    path = "../TextFolder/globalData"
    date = getFiles(path)
    nameDB = 'dataSummerInternship'
    nameTable = 'signals'
    mydb = connection()
    
    mycursor = mydb.cursor()
    createDB(nameDB,mycursor)
    mydb.connect(database = nameDB)
    createTable(nameTable,mycursor) 

    for i in date:
        insertInfo(nameTable, mycursor, 1, i, "?")
    


if __name__ == "__main__":
    main()


