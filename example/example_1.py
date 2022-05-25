import sqlite3

class Worker():
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.position = kwargs.get('position')
        self.work_from_date = kwargs.get('work_from_date')
        self.birth_date = kwargs.get('birth_date')

    def get_data(self):
        return self.name, self.position, self.work_from_date, self.birth_date


w1 = Worker(name='Petrov Vadym', position='manager', work_from_date='09-12-2019', birth_date='18-02-1990')
connection = sqlite3.connect('staff_db.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE staff (name text, position text, work_from_date text, birth_date text);')
cursor.execute("INSERT INTO staff VALUES ('Ivanov Ivan', 'nesalo', '07-10-2019', '2-12-1980');")
cursor.execute("INSERT INTO staff VALUES (?,?,?,?)", w1.get_data())
connection.commit()

all_workers = [('Borysov Mykola', 'ingeneer', '23-11-1976', '04-12-2019'),
               ('Pavlyik Inna', 'secretary', '12-09-1991', '22-01-2020'),
               ('Kolodych Leonid', 'ingeneer', '16-08-1986', '13-01-2020')]

cursor.executemany("INSERT INTO staff VALUES (?,?,?,?)", all_workers)
connection.commit()

print('Записи в таблиці бази даних у вигляді списка:')
sql = "SELECT * FROM staff"
cursor.execute(sql)

for line in cursor.fetchall():
    print(line)

sql = "UPDATE staff SET position = 'main ingeneer' WHERE name = 'Kolodych Leonid'"
cursor.execute(sql)
connection.commit()

print('Список всіх ingeneer:')

sql = "SELECT * FROM staff WHERE position=?"
cursor.execute(sql, [("ingeneer")])
for line in cursor.fetchall():
    print(line)

print('Список всіх записів в таблиці:')
for row in cursor.execute("SELECT rowid, * FROM staff ORDER BY name"):
    print(row)

