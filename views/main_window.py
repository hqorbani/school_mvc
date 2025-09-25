import ttkbootstrap as ttk
from ttkbootstrap.constants import * # TOP BOTH RIGHT...
from views.class_view.class_form_view import ClassFormView
from views.class_view.class_list_view import ClassListView
from controllers.class_controller.class_form_controller import ClassFormController
from controllers.class_controller.class_list_controller import ClassListController

from views.student_view.student_form_view import StudentFormView
from views.student_view.student_list_view import StudentListView
from controllers.student_controller.student_form_controller import StudentFormController
from controllers.student_controller.student_list_controller import StudentListController

from models.student_model import StudentModel
from models.class_model import ClassModel
from db.db_connection import Database
from db.db_schema import create_tables

from apps.rw_files import read_json_file

from views.enrollment_view.enrollment_form_view import EnrollmentFormView
from controllers.enrollment_controller.enrollment_form_controller import EnrollmentFormController
from models.enrollment_model import EnrollmentModel


class MainWindow(ttk.Window):
    def __init__(self):
        app_properties = read_json_file('json/app_properties.json')
        super().__init__(themename= app_properties['theme'] , title= app_properties['title'] , size=(600, 400))
        self.db = Database("database.db")
        create_tables(self.db)
        self.class_model = ClassModel(self.db)
        self.student_model = StudentModel(self.db)
        self.enrollment_model = EnrollmentModel(self.db)

        self._create_menu()
    
    def _create_menu(self):
        self.navbar = ttk.Frame(self)
        self.navbar.pack(side = TOP , fill= X)

        ttk.Button(self.navbar, text="ثبت کلاس" , command= self.show_class_form).pack(side=RIGHT , padx=1)
        ttk.Button(self.navbar, text=" کلاس ها" , command= self.show_class_list).pack(side=RIGHT , padx=1)

        ttk.Button(self.navbar, text="ثبت دانش آموز" , command= self.show_student_form).pack(side=RIGHT , padx=1)
        ttk.Button(self.navbar, text=" دانش آموزان" , command= self.show_student_list).pack(side=RIGHT , padx=1)
        ttk.Button(self.navbar, text="ثبت کلاس برای دانش‌آموز", command=self.show_enrollment_form).pack(side=RIGHT , padx=1)


        self.content = ttk.Frame(self)
        self.content.pack(fill=BOTH)

        self.show_class_form()
    
    def show_class_form(self):
        self._clear_content()
        view = ClassFormView(self.content)
        ClassFormController(self.class_model , view)

    def show_class_list(self):
        self._clear_content()
        view = ClassListView(self.content)
        ClassListController(self.class_model , view)

    def show_student_form(self):
        self._clear_content()
        view = StudentFormView(self.content)
        StudentFormController(self.student_model , view)

    def show_student_list(self):
        self._clear_content()
        view = StudentListView(self.content)
        StudentListController(self.student_model , view)
    
    def show_enrollment_form(self):
        self._clear_content()
        view = EnrollmentFormView(self.content)
        EnrollmentFormController(self.student_model, self.enrollment_model, view)

    def _clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()