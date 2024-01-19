from DtDb import DtDb
from DtGuiTk import DtGuiTk

def main():
    db = DtDb(init=False, dbName='DtDb.csv')
    app = DtGuiTk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()  