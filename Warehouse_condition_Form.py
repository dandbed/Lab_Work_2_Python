import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import WCF_helper as helper

class Warehouse_condition_Form(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Warehouse_condition_Form')
        self['background'] = '#776B5D'
        all_data=[]
        self.put_frames()

    def put_frames(self):
        self.WCF_frame = Param_Frame(self).grid(row=0, column=0, sticky='nswe')

    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            self.nametowidget(f_name).destroy()
        self.put_frames()
        self.WCF_frame = Table_Frame(self).grid(row=1, column=0, sticky='nswe')

class Param_Frame(tk.Frame):
     def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

     def put_widgets(self):
         self.l_date = ttk.Label(self, text="Выберете дату")
         self.f_date = DateEntry(self, date_pattern='dd-mm-YYYY')
         self.btn_output = ttk.Button(self, text="Вывести состояние склада по состаянию на введенную дату", command=self.Output)

         self.l_date.grid(row=0, column=0, sticky="w", padx=10, pady=10)
         self.f_date.grid(row=0, column=1, sticky="e", padx=10, pady=10)
         self.btn_output.grid(row=1, column=0, columnspan=2, sticky="n")

     def Output(self):
         date = helper.get_timestamp_from_string(self.f_date.get())
         self.master.all_data = helper.condition(date)
         self.master.refresh()

class Table_Frame(tk.Frame):
     def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

     def put_widgets(self):
         heads = ['name', 'amount']
         table = ttk.Treeview(self, show='headings')
         table['columns'] = heads

         for header in heads:
             table.heading(header, text=header, anchor='center')
             table.column(header, anchor='center')

         for row in helper.get_table_data(self.master.all_data):
             table.insert('', tk.END, values=row)
             table.pack(expand=tk.YES, fill=tk.BOTH)