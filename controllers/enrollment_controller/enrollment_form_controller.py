from messages.errors import ErrorMessages
from messages.successes import SuccessMessages
from tkinter import messagebox

class EnrollmentFormController:
    def __init__(self, student_model, class_model, enrollment_model, view):
        self.student_model = student_model
        self.class_model = class_model
        self.enrollment_model = enrollment_model
        self.view = view
        self.student_id = None

        self.view.fetch_button.config(command=self.fetch_student)
        self.view.enroll_button.config(command=self.enroll_classes)

    def fetch_student(self):
        code = self.view.get_national_code()
        student = self.student_model.get_by_national_code(code)
        if student:
            self.student_id = student[0]
            self.view.show_student(student[1] , student[2])
            classes = self.class_model.get_all_classes()
            enrolled_ids = self.enrollment_model.get_enrolled_class_ids(self.student_id)
            self.view.show_classes(classes, enrolled_ids)
        else:
            messagebox.showerror("خطا", ErrorMessages.STUDENT_NOT_FOUND)

    def enroll_classes(self):
        if not self.student_id:
            messagebox.showerror("خطا", ErrorMessages.STUDENT_NO_SELECTED)
            return
        selected = self.view.get_selected_classes()
        self.enrollment_model.update_student_enrollments(self.student_id, selected)
        messagebox.showinfo("موفقیت", SuccessMessages.SUCCESS_CLASS_REGISTRATION)
