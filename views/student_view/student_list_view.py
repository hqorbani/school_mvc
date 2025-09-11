import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StudentListView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.pack(fill=BOTH, expand=True)
        TreeViewCols = ("نام دانش آموز", "کد ملی","موبایل")
        self.tree = ttk.Treeview(self, columns= TreeViewCols, show="headings")
        for col in TreeViewCols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER)
        self.tree.pack(fill=BOTH, expand=True)

    def populate(self, student_list):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student_property in student_list:
            self.tree.insert("", "end", values=(
                student_property[1], student_property[2], student_property[3]
                ))
