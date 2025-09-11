import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ClassListView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.pack(fill=BOTH, expand=True)
        TreeViewCols = ("عنوان کلاس", "ظرفیت")
        self.tree = ttk.Treeview(self, columns= TreeViewCols, show="headings")
        for col in TreeViewCols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER)
        self.tree.pack(fill=BOTH, expand=True)

    def populate(self, class_list):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for class_property in class_list:
            self.tree.insert("", "end", values=(
                class_property[1], class_property[2]
                ))
