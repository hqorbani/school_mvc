class ClassListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.load_students()

    def load_students(self):
        students = self.model.get_all_classes()
        self.view.populate(students)
