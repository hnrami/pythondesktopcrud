from db_utils import setup_db
from gui_utils import create_gui

if __name__ == "__main__":
    # Set up the database
    setup_db()

    # Launch the GUI
    app = create_gui()
    app.mainloop()
