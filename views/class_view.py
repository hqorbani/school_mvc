import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class ClassView(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        self.capacity_entry = ttk.Entry(self)
        self.capacity_entry.pack(pady=5)

        add_btn = ttk.Button(self, text="افزودن کلاس", command=self.add_class)
        add_btn.pack(pady=5)

        self.class_list = ttk.Treeview(self, columns=("id", "name", "capacity"), show="headings")
        self.class_list.heading("id", text="ID")
        self.class_list.heading("name", text="نام کلاس")
        self.class_list.heading("capacity", text="ظرفیت")
        self.class_list.pack(fill="both", expand=True)

        self.refresh_class_list()

    def add_class(self):
        name = self.name_entry.get()
        try:
            capacity = int(self.capacity_entry.get())
            self.controller.create_class(name, capacity)
            self.refresh_class_list()
        except Exception as e:
            Messagebox.show_error(title="خطا", message=str(e))

    def refresh_class_list(self):
        for row in self.class_list.get_children():
            self.class_list.delete(row)
        for cls in self.controller.get_classes():
            self.class_list.insert("", "end", values=cls)
