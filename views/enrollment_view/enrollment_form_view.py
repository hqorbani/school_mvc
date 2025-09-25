import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class EnrollmentFormView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)
        self.pack(fill=BOTH, expand=True)
        self.class_vars = []

        ttk.Label(self, text="کد ملی دانش‌آموز:").pack(pady=5)
        self.national_code_entry = ttk.Entry(self)
        self.national_code_entry.pack(pady=5)

        self.fetch_button = ttk.Button(self, text="واکشی دانش‌آموز")
        self.fetch_button.pack(pady=5)

        self.student_label = ttk.Label(self, text="")
        self.student_label.pack(pady=5)

        self.class_frame = ttk.Frame(self)
        self.class_frame.pack(pady=10, fill=X)

        self.enroll_button = ttk.Button(self, text="ثبت کلاس‌ها", bootstyle=SUCCESS)
        self.enroll_button.pack(pady=10)

    def get_national_code(self):
        return self.national_code_entry.get()

    def show_student(self, name):
        self.student_label.config(text=f"دانش‌آموز: {name}")

    def show_classes(self, classes, enrolled_ids=None):
        enrolled_ids = enrolled_ids or []
        for widget in self.class_frame.winfo_children():
            widget.destroy()
        self.class_vars.clear()
        for cid, title in classes:
            var = ttk.BooleanVar(value=(cid in enrolled_ids))
            chk = ttk.Checkbutton(self.class_frame, text=title, variable=var)
            chk.pack(anchor=W)
            self.class_vars.append((cid, var))


    def get_selected_classes(self):
        return [cid for cid, var in self.class_vars if var.get()]
