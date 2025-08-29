from ttkbootstrap import Window
from db.db_connection import Database
from db.db_schema import create_tables
from models.class_model import ClassModel
from controllers.class_controller import ClassController
from views.class_view import ClassView

def main():
    db = Database()
    create_tables(db)

    class_model = ClassModel(db)
    class_controller = ClassController(class_model)

    app = Window(themename="flatly")
    ClassView(app, class_controller)
    app.mainloop()

    db.close()

# if __name__ == "__main__":
main()
