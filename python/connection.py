import pyodbc

try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-R089M73\SQLEXPRESS;DATABASE=manage;Trusted_Connection=yes;')
    print('concion sitosa')
    cursor = connection.cursor()
    cursor.execute('select * from usuarios;')
    row = cursor.fetchone()
    rows = cursor.fetchall()
    print(row)
    print(rows)
except Exception as ex:
    print(ex)