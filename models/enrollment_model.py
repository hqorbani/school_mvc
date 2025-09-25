class EnrollmentModel:
    def __init__(self, db):
        self.db = db

    def get_enrolled_class_ids(self, student_id):
        rows = self.db.fetchall("SELECT class_id FROM enrollments WHERE student_id = ?", (student_id,))
        return [row[0] for row in rows]
    
    # این متد مسئول همگام‌سازی ثبت‌نام دانش‌آموز با کلاس‌های انتخاب‌شده در فرم هست
    def update_student_enrollments(self, student_id, selected_class_ids):
        # واکشی کلاس‌های قبلی
        current_ids = self.get_enrolled_class_ids(student_id)

        # کلاس‌هایی که باید اضافه بشن
        to_add = set(selected_class_ids) - set(current_ids)
        # کلاس‌هایی که باید حذف بشن
        to_remove = set(current_ids) - set(selected_class_ids)
        
        # ثبت کلاس‌های جدید
        for class_id in to_add:
            try:
                self.db.execute("INSERT INTO enrollments (student_id, class_id) VALUES (?, ?)", (student_id, class_id))
            except:
                pass  # جلوگیری از ثبت تکراری

        for class_id in to_remove:
            self.db.execute("DELETE FROM enrollments WHERE student_id = ? AND class_id = ?", (student_id, class_id))

