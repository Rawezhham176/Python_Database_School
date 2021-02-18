import mysql.connector
import csv
import time
import sys
import logging

format = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
logging.basicConfig(filename="log_Py.log", level=logging.INFO, filemode="a", format=format)
'''logger = logging.getLogger("meinLogger")
logger.setLevel(logging.DEBUG)
fileh = logging.FileHandler("log.txt")
form = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')
fileh.setFormatter(form)
logger.addHandler(fileh)
logger.debug("debugging")'''

def time_fun(sec):
    time.sleep(sec)


def help_function():
    print("You need help? Hear is my support :)")
    print("You can always write a word or a sentence, what describe your intention. For example delete column or make a new table.")
    logging.info("Help function was activated")


def Server_connection():
    print("Please enter the connection data:")
    logging.info("Rhe user try to connect to the server")

    global connection
    condition = True
    while condition:
        try:
            host = input("Please input the host name: ")
            user = input("Please input the user name: ")
            password = input("Please input the password: ")
            # database = input("Please input the database name: ")

            stop_to_repeat = True

            while stop_to_repeat:

                connection = mysql.connector.connect(host=host,
                                                     user=user,
                                                     password=password
                                                     )
                global mycursor
                mycursor = connection.cursor(buffered=True)

                print("")
                mycursor.execute("SHOW DATABASES")
                print("Databases: ")
                for db in mycursor:
                    print(db)

                print("")

                num = True
                while num:
                    try:
                        print("1. Connect with a database\n"
                              "2. Make a new database")
                        answer = int(input("Please answer with 1 or 2: "))
                        if answer == 1 or answer == 2:
                            if answer == 2:
                                name_of_databse = input("Name of the new database: ")

                                sqlform = "CREATE DATABASE " + name_of_databse
                                mycursor.execute(sqlform)
                            else:
                                database = input("Please enter the database name: ")
                                connection = mysql.connector.connect(host=host,
                                                                     user=user,
                                                                     password=password,
                                                                     database=database)
                                mycursor = connection.cursor(buffered=True)
                                stop_to_repeat = False

                            num = False

                    except:
                        print("Please answer with a number 1 or 2!")
                        logging.error("An error with number input")

            if (connection):
                print("Connection successful")
                condition = False
                time_fun(1)

        except:
            print("Not connected")
            logging.critical("The logging information was not correct")


def table_make():
    condition = True
    print("Not forget, your table must have at least 1 column")

    while condition:
        try:
            tableN = input("Please enter the name of the new table: ")
            columns = int(input("How many columns do you want to make: "))
            i = 0

            while i < columns:
                columnsN = input("Please enter the columns name: ")
                columnsT = input("Please enter the columns type: ")
                i = i + 1

                if i == 1:
                    sqlform = "CREATE TABLE " + tableN + "(" + columnsN + " " + columnsT + ")"
                else:
                    sqlform = "ALTER TABLE " + tableN + " ADD " + columnsN + " " + columnsT

                mycursor.execute(sqlform)
            if i == columns:
                condition = False

        except:
            print("Please try again!")


def table_delete():
    try:
        tableN = input("Please enter the table name: ")

        sqlform = "DROP TABLE " + tableN

        mycursor.execute(sqlform)
    except:
        print("Please check if the table really exist!")


def show_table():
    sqlformp = "SHOW TABLES"
    mycursor.execute(sqlformp)

    for tb in mycursor:
        print(tb)


def columns_make():
    try:
        tableN = input("Please enter the table name:")

        columns = int(input("How many columns do you want to make: "))
        i = 0

        while i < columns:
            columnsN = input("Please enter the columns name: ")
            columnsT = input("Please enter the columns type: ")

            sqlform = "ALTER TABLE " + tableN + " ADD " + columnsN + " " + columnsT

            mycursor.execute(sqlform)
            i = + 1
    except:
        print("Please make sure that you gave the correct input!")


def columns_drop():
    try:
        tableN = input("Please input the name of the table:")
        columnN = input("Please enter the name of the column you want to delete: ")

        sqlform = "ALTER TABLE " + tableN + " DROP COLUMN " + columnN

        mycursor.execute(sqlform)
    except:
        print("Please make sure that you gave correct input or if the column exist!")


def show_columns():
    try:
        tableN = input("Please enter the table name: ")

        sqlform = "SHOW COLUMNS FROM " + tableN

        mycursor.execute(sqlform)

        for tb in mycursor:
            print(tb)
    except:
        print("Please make sure that the input is correct!")


def addition_to_table():
    try:
        tableN = input("Please enter the name of the table:")
        sqlform = "SHOW COLUMNS FROM " + tableN
        mycursor.execute(sqlform)

        columnN = input("Please enter the name of the column, which you want to add the information: ")

        addition_text = input("Pleas enter what you want to add to the " + columnN + ": ")

        if addition_text.isdigit():
            sqlform = "INSERT INTO " + tableN + " (" + columnN + ")" + "VALUES" + "(" + addition_text + ")"
        else:
            sqlform = "INSERT INTO " + tableN + " (" + columnN + ")" + "VALUES" + "(\"" + addition_text + "\")"

        mycursor.execute(sqlform)
        connection.commit()

    except:
        print("Please make sure that the input is correct!")

    '''        i = 0
            for tb in mycursor:
                print(tb)
                i = +1
    '''

    '''        t = 0
        b = 0
        more = True

        while more:
            while t < i - 1:
                more_info = input(
                    "Do you want to add information to another column in the same row? you can write the column name or 0 for no: ")

                    more = False
                else:
                    column_2 = input("Pleas enter the column name: ")
                    b =+ 1
    '''

    '''   
     if b == 1:
            addition_text_one = input("Pleas enter what you want to add to the " + columnN + ": ")
            addition_text_tow = input("Pleas enter what you want to add to the " + columnN + ": ")
            
            if addition_text_one.isdigit():
                sqlform = "INSERT INTO " + tableN + " (" + columnN + ")" + "VALUES" + "(" + addition_text + ")"
            else:
                sqlform = "INSERT INTO " + tableN + " (" + columnN + ")" + "VALUES" + "(\"" + addition_text + "\")"

    '''


def alter_some_inTable():
    tableN = input("Please enter the name of the table: ")
    sqlform = "SHOW COLUMNS FROM " + tableN
    mycursor.execute(sqlform)

    columnN = input("Please enter the name of the column, which you want to add information: ")
    add_to_column = input("Pleas enter what you want to add: ")

    columnC = input("Please enter the name of the column for the condition: ")
    condition_text = input("Please enter the condition: ")

    sqlform = "UPDATE " + tableN + " SET " + columnN + "= %s WHERE " + columnC + "= %s"
    values = (add_to_column, condition_text)

    mycursor.execute(sqlform, values)
    connection.commit()


def delete_from_table():
    try:
        tableN = input("Please input the name of the table:")
        columnN = input("Please enter the name of the column: ")
        delete_item = input("Pleas enter what you want to delete: ")

        sqlform = "DELETE FROM  " + tableN + " WHERE " + columnN + "=" + delete_item
        mycursor.execute(sqlform)
        connection.commit()
    except:
        print("Please make sure that the input is correct!")


def show_data():
    global tableNS
    tableNS = input("Please enter tne table name: ")

    sqlform = "SELECT * FROM " + tableNS

    mycursor.execute(sqlform)

    global res
    res = mycursor.fetchall()

    for row in res:
        print(row)


def save_data():
    with open("mydata.txt", "a") as file:
        file.write("The table " + tableNS + "H has: \n")
        for row in res:
            csv.writer(file).writerow(row)


def end_fun():
    print("That was fun with you :). I hope i see you again.")
    sys.exit(0)


def switch_function(num):
    if num == "0" or num == "end" or num == "exit":
        end_fun()
    if num == "1" or num == "show the tables" or num == "tables" or num == "tables show":
        show_table()
    elif num == "2" or num == "make a table" or num == "table make" or num == "make a new table":
        table_make()
    elif num == "3" or num == "delete a table" or num == "table delete":
        table_delete()

    elif num == "4" or num == "show the columns" or num == "columns" or num == "columns show":
        show_columns()
    elif num == "5" or num == "make a column" or num == "column make" or num == "make a new column":
        columns_make()
    elif num == "6" or num == "delete a column" or num == "column delete":
        columns_drop()

    elif num == "7" or num == "show the data" or num == "data" or num == "data show":
        show_data()
        save_data()
    elif num == "8" or num == "add" or num == "add something" or num == "something add":
        addition_to_table()
    elif num == "9":
        alter_some_inTable()
    elif num == "10" or num == "delete something" or num == "something delete":
        delete_from_table()

    elif num == "11" or num == "help" or num == "help me" or num == "-help" or num == "--help":
        help_function()
