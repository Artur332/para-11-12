import sqlite3

connect = sqlite3.connect('employees')

cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id TEXT ,name TEXT ,position TEXT ,salary REAL)''')

employees_data = [( 'Max', 'Manager', 22000),( 'Artur', "Manager", 19000),('Danulo', 'Manager', 23000)]
cursor.executemany('INSERT INTO employees ', employees_data)

connect.commit()


cursor.execute('SELECT * FROM employees')
employees = cursor.fetchall()

print("Employees:")
for employee in employees:
    print(employee)

connect.close()