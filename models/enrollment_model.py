class EnrollmentModel:
    def __init__(self, db):
        self.db = db

    def enroll_student(self, student_id, class_id):
        self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))

    def enroll_student_in_classes(self, student_id, class_ids):
        for class_id in class_ids:
            try:
                self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))
            except:
                pass  # جلوگیری از ثبت تکراری

    def get_enrollments(self):
        return self.db.fetchall("""
            SELECT e.id, s.name, c.name
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            JOIN classes c ON e.class_id = c.id
        """)

    def get_all_classes(self):
        return self.db.fetchall("SELECT id, name FROM classes")

    def get_enrolled_class_ids(self, student_id):
        rows = self.db.fetchall("SELECT class_id FROM enrollments WHERE student_id = ?", (student_id,))
        return [row[0] for row in rows]
    
    def update_student_enrollments(self, student_id, selected_class_ids):
        # واکشی کلاس‌های قبلی
        current_ids = self.get_enrolled_class_ids(student_id)

        # کلاس‌هایی که باید اضافه بشن
        to_add = set(selected_class_ids) - set(current_ids)
        # کلاس‌هایی که باید حذف بشن
        to_remove = set(current_ids) - set(selected_class_ids)

        for class_id in to_add:
            try:
                self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))
            except:
                pass  # جلوگیری از ثبت تکراری

        for class_id in to_remove:
            self.db.execute("DELETE FROM enrollments WHERE student_id = ? AND class_id = ?", (student_id, class_id))

