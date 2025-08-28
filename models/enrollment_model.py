class EnrollmentModel:
    def __init__(self, db):
        self.db = db

    def enroll_student(self, student_id, class_id):
        self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))

    def get_enrollments(self):
        return self.db.fetchall("""
            SELECT e.id, s.name, c.name
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            JOIN classes c ON e.class_id = c.id
        """)
