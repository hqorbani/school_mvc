class StudentListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.load_student_list()

    def load_student_list(self):
        students = self.model.get_all_students()
        self.view.populate(students)
