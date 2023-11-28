import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
import LoSF_helper as helper
class List_of_Suppliers_Form(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('List_of_Suppliers_Form')
        self['background'] = '#D0A2F7'
        all_data=[]
        self.put_frames()

    def put_frames(self):
        self.LoSF_frame = Param_Frame(self).grid(row=0, column=0, sticky='nswe')
        #self.LoSF_frame = Table_Frame(self).grid(row=1, column=0, sticky='nswe')

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()
        self.LoSF_frame = Table_Frame(self).grid(row=1, column=0, sticky='nswe')

class Param_Frame(tk.Frame):
    def __init__(self, parent):
            super().__init__(parent)
            self['background'] = self.master['background']
            self.items=self.get_all_category()
            items = self.get_all_category()
            self.put_widgets()

    def get_all_category(self):
        all_data = {'accordance': {}, 'category': []}
        result = {}
        with sqlite3.connect('Lab_Work_2.db') as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            query = """SELECT id, category FROM items GROUP BY category"""
            cursor.execute(query)
            result = dict(cursor)
        all_data['accordance'] = {result[k]: k for k in result}
        all_data['category'] = [v for v in result.values()]
        return all_data

    def put_widgets(self):
        self.l_category = ttk.Label(self, text="Выберите категорию товаров")
        self.c_category=ttk.Combobox(self, values=self.items['category'])
        self.l_start_date = ttk.Label(self, text="Выберете начальную дату")
        self.f_start_date = DateEntry(self, date_pattern='dd-mm-YYYY')
        self.l_end_date = ttk.Label(self, text="Выберете конечную дату")
        self.f_end_date = DateEntry(self, date_pattern='dd-mm-YYYY')
        self.btn_output = ttk.Button(self, text="Вывести количество товаров", command=self.Output)

        self.l_category.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.c_category.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        self.l_start_date.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.f_start_date.grid(row=1, column=1, sticky="e", padx=10, pady=10)
        self.l_end_date.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.f_end_date.grid(row=2, column=1, sticky="e", padx=10, pady=10)
        self.btn_output.grid(row=3, column=0, columnspan=2, sticky="n")

    def Output(self):
        category = self.c_category.get()
        start_date = helper.get_timestamp_from_string(self.f_start_date.get())
        end_date = helper.get_timestamp_from_string(self.f_end_date.get())
        self.master.all_data=helper.checking_conditions(category, start_date, end_date)
        self.master.refresh()

class Table_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ['id', 'name', 'delivery_date', 'amount', 'provider']
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in self.master.all_data:
            table.insert('', tk.END, values=row)
            table.pack(expand=tk.YES, fill=tk.BOTH)