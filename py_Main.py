#!/usr/bin/python3
import py_Programm_Classes as pc

print("Hello. Welcome to the program.")
print("At first, you have to connect with your Server.\n")
pc.Server_connection()

print("\nYou can chose a number or write what you want to do.")
answer = "10"
while answer != "0":
    print("1. Show the tables\n"
          "2. Make a new table\n"
          "3. Delete a table\n"
          "4. Show the columns from a table\n"
          "5. Make a new column in a table\n"
          "6. Delete a column from a table\n"
          "7. Show data from a table\n"
          "8. Add something to a table\n"
          "9. Alter some information from a column\n"
          "10.Delete something from a table\n"
          "11.Help \n"
          "0. End \n")
    answer = input("Your input: ")
    pc.switch_function(answer)
    print("")