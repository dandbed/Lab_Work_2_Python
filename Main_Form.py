import tkinter as tk
from tkinter import ttk
import Warehouse_condition_Form as WCF
import List_of_Suppliers_Form as LoSF
import Filter_Form as FF

class Main_Form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Main Form')
        self['background']='#A6CF98'
        self.put_widgets()

    def put_widgets(self):
        self.btn_WCF=ttk.Button(self, text="Окно просмотра состояния скалада", command=self.btn_WCF_clicked)
        self.btn_LoSF=ttk.Button(self, text="Окно посмотра списка поставщиков", command=self.btn_LoSF_clicked)
        self.btn_FF=ttk.Button(self, text="Окно просмотра по фильтру", command=self.btn_FF_clicked)

        self.btn_WCF.grid(row=0, column=0, padx=10, pady=10)
        self.btn_LoSF.grid(row=1, column=0, padx=10, pady=10)
        self.btn_FF.grid(row=2, column=0, padx=10, pady=10)

    def btn_WCF_clicked(self):
        wcf=WCF.Warehouse_condition_Form()

    def btn_LoSF_clicked(self):
        losf=LoSF.List_of_Suppliers_Form()

    def btn_FF_clicked(self):
        ff=FF.Filter_Form()

app=Main_Form()
app.mainloop()
