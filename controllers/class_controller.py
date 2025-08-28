from messages.errors import ErrorMessages

class ClassController:
    def __init__(self, model):
        self.model = model

    def create_class(self, name, capacity):
        if not name:
            raise ValueError(ErrorMessages.INVALID_CLASS_NAME)
        if capacity <= 0:
            raise ValueError(ErrorMessages.INVALID_CAPACITY)
        self.model.add_class(name, capacity)

    def get_classes(self):
        return self.model.get_all_classes()

    def update_class(self, class_id, name, capacity):
        self.model.update_class(class_id, name, capacity)

    def delete_class(self, class_id):
        self.model.delete_class(class_id)
