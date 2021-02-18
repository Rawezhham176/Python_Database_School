import mysql.connector

ct = mysql.connector.connect(host='localhost', user='ghost', password='MySql12345$&*', db='school_project', auth_plugin='mysql_native_password')
cursor = ct.cursor()

print(ct)