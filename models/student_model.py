class StudentModel:
    def __init__(self, db):
        self.db = db

    def add_student(self, name , national_code , mobile , password):
        self.db.execute("INSERT INTO students (name, national_code , mobile , password) VALUES (?,?,?,?)"
                        , (name, national_code , mobile , password))

    def get_all_students(self):
        return self.db.fetchall("SELECT id, name, national_code , mobile FROM students")

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id = ?", (student_id,))

    def get_by_national_code(self, code):
        return self.db.fetchone("SELECT id, name FROM students WHERE national_code = ?", (code,))

