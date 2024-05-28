ЗАВДАННЯ 2

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self):
        pass

class Pawn(Piece):
    def move(self):
        print("пішак рухається на 1 або 2 клітини і атакує по діагоналі")

class Rook(Piece):
    def move(self):
        print("Тура рухається горизонтально або вертикально")

class Knight(Piece):
    def move(self):
        print("Кінь рухається у формі «L»")

class Bishop(Piece):
    def move(self):
        print("Слон рухається по діагоналі на будьяку кількість полів")

class Queen(Piece):
    def move(self):
        print("королева рухається по горизонталі або по вертикалі")

class King(Piece):
    def move(self):
        print("король рухається на 1 клітку в любому напрямку")

pawn = Pawn("Білий", "A2")
rook = Rook("Чорний", "H8")
knight = Knight("Білий", "G1")
bishop = Bishop("Чоринй", "C3")
queen = Queen("Білий", "D4")
king = King("Чорний", "E5")

pieces = [pawn, rook, knight, bishop, queen, king]

for piece in pieces:
    print(f"{piece.color} {piece.__class__.__name__} at position {piece.position}:")
    piece.move()

#ЗАВДЯННЯ 3

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
