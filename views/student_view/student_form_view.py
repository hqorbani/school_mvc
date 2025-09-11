import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StudentFormView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)
        self.pack(fill=BOTH, expand=True)

        # grid 3x2
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=0, row=0, sticky= EW, padx=2, pady=5)
        self.name_label = ttk.Label(self, text="نام ").grid(column=1, row=0, sticky= E, padx=10, pady=5)

        self.national_code_entry = ttk.Entry(self)
        self.national_code_entry.grid(column=0, row=1, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="کد ملی").grid(column=1, row=1, sticky= E, padx=10, pady=5)

        self.mobile_entry = ttk.Entry(self)
        self.mobile_entry.grid(column=0, row=2, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="موبایل").grid(column=1, row=2, sticky= E, padx=10, pady=5)

        self.password_entry = ttk.Entry(self)
        self.password_entry.grid(column=0, row=3, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="رمز ورود").grid(column=1, row=3, sticky= E, padx=10, pady=5)

        self.save_button = ttk.Button(self, text="ثبت", bootstyle=SUCCESS)
        self.save_button.grid(column=0, row=4, columnspan=2, sticky= EW, padx=2, pady=5)


    def get_student_form(self):
        return{
            "name" : self.name_entry.get(),
            "national_code" : self.national_code_entry.get(),
            "mobile" : self.mobile_entry.get(),
            "password" : self.password_entry.get()
        }
        
