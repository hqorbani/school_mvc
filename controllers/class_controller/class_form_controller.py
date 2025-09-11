from messages.errors import ErrorMessages
from tkinter import messagebox

class ClassFormController:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        self.view.save_button.config(command=self.save_form)

    def save_form(self):
        try:
            data = self.view.get_class_form()
            self.model.add_class(data["name"], data["capacity"])
            messagebox.showinfo("موفقیت", "دانش‌آموز با موفقیت ثبت شد.")
        except Exception as e:
            messagebox.showerror("خطا", f"ثبت‌نام انجام نشد: {e}")

    def get_classes(self):
        return self.model.get_all_classes()

    def update_class(self, class_id, name, capacity):
        self.model.update_class(class_id, name, capacity)

    def delete_class(self, class_id):
        self.model.delete_class(class_id)
