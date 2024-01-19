'''
This is the interface to an SQLite Database
'''

import sqlite3

class DtDbSqlite:
    def __init__(self, dbName='Dates.db'):
        super().__init__()
        self.dbName = dbName
        self.csvFile = self.dbName.replace('.db', '.csv')
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dates (
                id TEXT PRIMARY KEY,
                event TEXT,
                month TEXT,
                day TEXT,
                location TEXT)''')
        self.conn.commit()
        self.conn.close()

    def connect_cursor(self):
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()        

    def commit_close(self):
        self.conn.commit()
        self.conn.close()        

    def create_table(self):
        self.connect_cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Dates (
                    id TEXT PRIMARY KEY,
                    event TEXT,
                    month TEXT,
                    day TEXT,
                    location TEXT)''')
        self.commit_close()

    def fetch_dates(self):
        self.connect_cursor()
        self.cursor.execute('SELECT * FROM Dates')
        dates =self.cursor.fetchall()
        self.conn.close()
        return dates

    def insert_date(self, id, event, month, day, location):
        self.connect_cursor()
        self.cursor.execute('INSERT INTO Dates (id, event, month, day, location) VALUES (?, ?, ?, ?, ?)',
                    (id, event, month, day, location))
        self.commit_close()

    def delete_date(self, id):
        self.connect_cursor()
        self.cursor.execute('DELETE FROM Dates WHERE id = ?', (id,))
        self.commit_close()

    def update_date(self, new_event, new_month, new_day, new_location, id):
        self.connect_cursor()
        self.cursor.execute('UPDATE Dates SET event = ?, month = ?, day = ?, location = ? WHERE id = ?',
                    (new_event, new_month, new_day, new_location, id))
        self.commit_close()

    def id_exists(self, id):
        self.connect_cursor()
        self.cursor.execute('SELECT COUNT(*) FROM Dates WHERE id = ?', (id,))
        result =self.cursor.fetchone()
        self.conn.close()
        return result[0] > 0        

    def export_csv(self):
        with open(self.csvFile, "w") as filehandle:
            dbEntries = self.fetch_dates()
            for entry in dbEntries:
                print(entry)
                filehandle.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]}\n")

'''
def test_EmpDb():
    iEmpDb = DtDbSqlite(dbName='DtDbSql.db')

    for entry in range(30):
        iEmpDb.insert_date(entry, f'Name{entry} Surname{entry}', f'SW Engineer {entry}', 'Male', 'On-Site')
        assert iEmpDb.id_exists(entry)

    all_entries = iEmpDb.fetch_employees()
    assert len(all_entries) == 30

    for entry in range(10, 20):
        iEmpDb.update_employee(f'Name{entry} Surname{entry}', f'SW Engineer {entry}', 'Female', 'Remote', entry)
        assert iEmpDb.id_exists(entry)

    all_entries = iEmpDb.fetch_employees()
    assert len(all_entries) == 30

    for entry in range(10):
        iEmpDb.delete_employee(entry)
        assert not iEmpDb.id_exists(entry) 

    all_entries = iEmpDb.fetch_employees()
    assert len(all_entries) == 20
'''