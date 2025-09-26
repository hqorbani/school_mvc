class ClassModel:
    def __init__(self, db):
        self.db = db

    def add_class(self, name, capacity):
        self.db.execute("INSERT INTO classes (name, capacity) VALUES (?, ?)", (name, capacity))

    def get_all_classes(self):
        return self.db.fetchall("SELECT id, name FROM classes")

    def update_class(self, class_id, name, capacity):
        self.db.execute("UPDATE classes SET name = ?, capacity = ? WHERE id = ?", (name, capacity, class_id))

    def delete_class(self, class_id):
        self.db.execute("DELETE FROM classes WHERE id = ?", (class_id,))
