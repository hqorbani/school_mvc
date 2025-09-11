import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ClassFormView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)
        self.pack(fill=BOTH, expand=True)

        # grid 3x2
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=0, row=0, sticky= EW, padx=2, pady=5)
        self.name_label = ttk.Label(self, text="نام کلاس").grid(column=1, row=0, sticky= E, padx=10, pady=5)
        

        self.capacity_entry = ttk.Entry(self)
        self.capacity_entry.grid(column=0, row=1, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="ظرفیت").grid(column=1, row=1, sticky= E, padx=10, pady=5)

        self.save_button = ttk.Button(self, text="ثبت", bootstyle=SUCCESS)
        self.save_button.grid(column=0, row=2, columnspan=2, sticky= EW, padx=2, pady=5)


    def get_class_form(self):
        return{
            "name" : self.name_entry.get(),
            "capacity" : int(self.capacity_entry.get())
        }
        
