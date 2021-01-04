import mysql.connector
import csv
import logging
import time
import pandas as pd
from pandas import DataFrame


'''
logging.debug("debugging")
logging.info("Info")
logging.error("Error")
logging.critical("Critical")
'''


def Set_time(num):
    time.sleep(num)

mydb = mysql.connector.connect(host="localhost",
                               user="Dracula",
                               password="Hawre$%&2020",
                               database="schoolproject")

mycursor = mydb.cursor()



print("Do you want to add something to the table?")
answer = input("Pleas enter one number 1 for yes 2 for no: ")

if answer != "1":
    pass
else:
    n = input("Please enter your addition for the name: ")
    s = int(input("Please enter your addition for the salary: "))

    sql = "insert into employee(name, sal) values(%s, %s)"
    val = (n, s)
    mycursor.execute(sql, val)
    mydb.commit()



answer = input("Do you want to see the text data? 1 for yes and 2 for no ")
if answer != "1":
    print("See you later")
else:
    logger = logging.getLogger("show_table")
    logger.setLevel(logging.DEBUG)
    logger.debug("in the function")

    sql = "select * from employee"

    mycursor.execute(sql)

    res = mycursor.fetchall()

    with open("mydata.txt", "w") as file:
        for row in res:
            csv.writer(file).writerow(row)

    f = open("mydata.txt", "r")
    mytab = pd.DataFrame(res)

    # print(f.read())
    print(mytab.to_string(index=False, header=False))
    time1 = Set_time(10)
