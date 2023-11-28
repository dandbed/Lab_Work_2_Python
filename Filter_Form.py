import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox

class Filter_Form(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Filter_Form')
        self['background'] = '#363062'
        self.put_frames()
        all_data=[]

    def put_frames(self):
        self.filter_form_frame=Filter_Frame(self).grid(row=0, column=0, sticky='nswe')

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()
        self.filter_form_frame = Table_Frame(self).grid(row=1, column=0, sticky='nswe')

class Filter_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.l_search = ttk.Label(self, text="Введите подстроку для нахождения товара")
        self.e_search = ttk.Entry(self, justify=tk.RIGHT)
        self.btn_find=ttk.Button(self, text='Поиск', command=self.Search_for_Matches)

        self.l_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.e_search.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        self.btn_find.grid(row=1, column=0, columnspan=2, sticky="n")

    def Search_for_Matches(self):
        Str_for_search = '%' + self.e_search.get() + '%'
        self.master.all_data = []
        with sqlite3.connect('Lab_Work_2.db') as db:
            cursor=db.cursor()
            query="""SELECT id, name FROM items WHERE name LIKE :name"""
            cursor.execute(query, {"name": Str_for_search})
            self.master.all_data=cursor
        self.master.refresh()

class Table_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        heads = ['id', 'name']
        table = ttk.Treeview(self, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for row in self.master.all_data:
            table.insert('', tk.END, values=row)
            table.pack(expand=tk.YES, fill=tk.BOTH)