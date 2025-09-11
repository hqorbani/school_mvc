class ClassListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.load_class_list()

    def load_class_list(self):
        students = self.model.get_all_classes()
        self.view.populate(students)
