from DtDbEntry import DtDbEntry
import csv
from tkinter import filedialog

class DtDb:

    def __init__(self, init=False, dbName='DtDb.csv'):

        self.dbName = dbName
        self.entries=[]


    def fetch_dates(self):

        dates=[]
        for x in self.entries:
            dates.append((x.id, x.event, x.month, x.day, x.location))

        return dates


    def insert_date(self, id, event, month, day, location):

        newEntry = DtDbEntry(id=id, event=event, month=month, day=day, location=location)
        self.entries.append(newEntry)

    def delete_date(self, id):

        for x in self.entries:
            if getattr(x,'id')==id:
                self.entries.remove(x)


    def update_date(self, new_event, new_month, new_day, new_location, id):

        editentry = DtDbEntry(event=new_event, month=new_month, day=new_day, location=new_location, id=id)

        for x in self.entries:
            if getattr(x,'id')==id:
                self.entries.remove(x)
                self.entries.append(editentry)

    def import_csv(self):
        self.entries.clear()
        fil=filedialog.askopenfilename(title='Open CSV', filetypes=(('CSV File','*.csv'),('All Files', '*.*')))
        with open(fil) as file:
            csv_reader=csv.reader(file, delimiter=',')
            for row in csv_reader:
                newId=row[0]
                newEvent=row[1]
                newMonth=row[2]
                newDay=row[3]
                newLocation=row[4]
                self.insert_date(newId, newEvent, newMonth, newDay, newLocation)


    def export_csv(self):

        with open(self.dbName, "w") as file:
            for x in self.entries:
                file.write(f"{x.id},{x.event},{x.month},{x.day},{x.location} \n")

    def id_exists(self, id):
       
        for x in self.entries:
            if getattr(x,'id')==id:
                return True
            else:
                return False

        
