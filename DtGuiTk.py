from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from DtDbSqlite import DtDbSqlite
from PIL import ImageTk, Image
import customtkinter

class DtGuiTk(Tk):

    def __init__(self, dataBase=DtDbSqlite('AppDb.db')):
        super().__init__()
        self.db = dataBase

        #specifications
        self.title('Date Tracker')
        self.geometry('1100x400')
        self.config(bg='#6e3b3b') 
        self.resizable(False, False)
        self.iconbitmap('cal.ico')

        self.font1 = ('Tahoma', 15, 'bold')
        self.font2 = ('Tahoma', 7, 'bold')

        #labels for entry fields and entry fields itself
        self.id_label = self.newCtkLabel('ID')
        self.id_label.place(x=55, y=40)
        self.id_entryVar = StringVar()
        self.id_entry = self.newCtkEntry(entryVariable=self.id_entryVar)
        self.id_entry.place(x=90, y=40)

        self.event_label = self.newCtkLabel('Event')
        self.event_label.place(x=37, y=70)
        self.event_entryVar = StringVar()
        self.event_entry = self.newCtkEntry(entryVariable=self.event_entryVar)
        self.event_entry.place(x=90, y=70)

        self.month_label = self.newCtkLabel('Month')
        self.month_label.place(x=30, y=130)
        self.month_cboxVar = StringVar()
        self.month_cboxOptions = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.month_cbox = self.newCtkComboBox(options=self.month_cboxOptions, 
                                    entryVariable=self.month_cboxVar)
        self.month_cbox.place(x=90, y=130)

        self.day_label = self.newCtkLabel('Day')
        self.day_label.place(x=46, y=160)
        self.day_entryVar = StringVar()
        self.day_entry = self.newCtkEntry(entryVariable=self.day_entryVar)
        self.day_entry.place(x=90, y=160)

        self.location_label = self.newCtkLabel('Location')
        self.location_label.place(x=20, y=220)
        self.location_entryVar = StringVar()
        self.location_entry = self.newCtkEntry(entryVariable=self.location_entryVar)
        self.location_entry.place(x=90, y=220)

        #function buttons
        self.add_button = self.newCtkButton(text='Add Date',
                                onClickHandler=self.add_entry,
                                fgColor='#feff89',
                                hoverColor='#ff9f68',
                                borderColor='#88bef5')
        self.add_button.place(x=875,y=45)


        self.new_button = self.newCtkButton(text='New Date',
                                onClickHandler=lambda:self.clear_form(True))
        self.new_button.place(x=875,y=115)


        self.update_button = self.newCtkButton(text='Update Date',
                                    onClickHandler=self.update_entry)
        self.update_button.place(x=875,y=185)


        self.delete_button = self.newCtkButton(text='Delete Date',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#f85959',
                                    hoverColor='#ff9f68',
                                    borderColor='#E40404')
        self.delete_button.place(x=875,y=255)


        self.export_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv)
        self.export_button.place(x=875,y=325)

        self.exit_button = self.newCtkButton(text='Exit',
                                    onClickHandler=self.quit)
        self.exit_button.place(x=70,y=325)

        self.import_button = self.newCtkButton(text='Import CSV',
                                               onClickHandler=self.import_csv)
        self.import_button.place(x=70, y=275)



        #database view
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#6e3b3b',
                        background='#f3cf7a',
                        fieldlbackground='#313837')

        self.style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('ID', 'Event', 'Month', 'Day', 'Location')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=20)
        self.tree.column('Event', anchor=tk.CENTER, width=130)
        self.tree.column('Month', anchor=tk.CENTER, width=110)
        self.tree.column('Day', anchor=tk.CENTER, width=40)
        self.tree.column('Location', anchor=tk.CENTER, width=140)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Event', text='Event')
        self.tree.heading('Month', text='Month')
        self.tree.heading('Day', text='Day')
        self.tree.heading('Location', text='Location')

        self.tree.place(x=330, y=18, width=500, height=350)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()


    #widgets
    def newCtkLabel(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#FFF'
        widget_BgColor='#2c1608'

        widget = ttk.Label(self, 
                        text=text)
        return widget

    def newCtkEntry(self, text = 'CTK Label', entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#f4cf7a'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=25

        widget = ttk.Entry(self, textvariable=entryVariable, width=widget_Width)
        return widget

    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#f3cf7a'
        widget_DropdownHoverColor='#0C9295'
        widget_ButtonColor='#0C9295'
        widget_ButtonHoverColor='#be6a15'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=200
        widget_Options=options

        widget = customtkinter.CTkComboBox(self, 
                              font=widget_Font,
                              text_color=widget_TextColor,
                              fg_color=widget_FgColor,
                              button_color=widget_ButtonColor,
                              button_hover_color=widget_ButtonHoverColor,
                              variable=entryVariable,
                              values=options,
                              state='readonly',
                              width=widget_Width)
        
        widget['values'] = tuple(options)
        return widget

    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#f3cf7a', hoverColor='#be6a15', bgColor='#6e3b3b', borderColor='#F15704'):
        widget_Font=self.font1
        widget_TextColor='#FFF'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=15
        widget_Width=25
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                            text=text,
                            command=widget_Function,
                            font=widget_Font,
                            text_color=widget_TextColor,
                            fg_color=widget_FgColor,
                            hover_color=widget_HoverColor,
                            bg_color=widget_BackgroundColor,
                            cursor=widget_Cursor,
                            corner_radius=widget_CornerRadius,
                            width=widget_Width)
       
        return widget



    #Handles
    def add_to_treeview(self):
        dates = self.db.fetch_dates()
        self.tree.delete(*self.tree.get_children())
        for date in dates:
            print(date)
            self.tree.insert('', END, values=date)


    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.id_entryVar.set('')
        self.event_entryVar.set('')
        self.month_cboxVar.set('January')
        self.day_entryVar.set('')
        self.location_entryVar.set('')


    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.id_entryVar.set(row[0])
            self.event_entryVar.set(row[1])
            self.month_cboxVar.set(row[2])
            self.day_entryVar.set(row[3])
            self.location_entryVar.set(row[4])
        else:
            pass


    #functions
    def add_entry(self):
        id=self.id_entryVar.get()
        event=self.event_entryVar.get()
        month=self.month_cboxVar.get()
        day=self.day_entryVar.get()
        location=self.location_entryVar.get()

        if not (id and event and month and day and location):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.id_exists(id):
            messagebox.showerror('Error', 'ID already exists')
        else:
            self.db.insert_date(id, event, month, day, location)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a date to delete')
        else:
            id = self.id_entryVar.get()
            self.db.delete_date(id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a date to update')
        else:
            id=self.id_entryVar.get()
            event=self.event_entryVar.get()
            month=self.month_cboxVar.get()
            day=self.day_entryVar.get()
            location=self.location_entryVar.get()
            self.db.update_date(event, month, day, location, id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been updated')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}.csv')
    
    def import_csv(self):
        self.db.import_csv()
        messagebox.showinfo('Succes', 'Data has been imported')






