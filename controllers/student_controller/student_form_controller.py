from messages.errors import ErrorMessages
from tkinter import messagebox

class StudentFormController:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        self.view.save_button.config(command=self.save_form)

    def save_form(self):
        try:
            data = self.view.get_student_form()
            self.model.add_student(data["name"], data["national_code"], data["mobile"], data["password"])
            messagebox.showinfo("موفقیت", "دانش‌آموز با موفقیت ثبت شد.")
        except Exception as e:
            messagebox.showerror("خطا", f"ثبت‌نام انجام نشد: {e}")


    def get_students(self):
        return self.model.get_all_students()

    def update_student(self, student_id, name, capacity):
        self.model.update_student(student_id, name, capacity)

    def delete_student(self, student_id):
        self.model.delete_student(student_id)
