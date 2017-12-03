# written by Vaishali



from controller import Controller
from employee import Employee
from command_view import CommandView
from view_csv_file import CsvFileView
from view_database import DatabaseView
from view_pickle import PickleView


if __name__ == "__main__":
    cmd_view = CommandView()
    csv_view = CsvFileView()
    pickle_view = PickleView()
    database_view = DatabaseView()
    view_list = [csv_view, database_view, pickle_view]
    # running controller function
    ctrl = Controller(view_list, cmd_view, Employee())
    # set the controller so cmd_view can call methods within the controller
    cmd_view.set_controller(ctrl)
    ctrl.start()


from controller import Controller
from employee import Employee
from command_view import CommandView
from view_csv_file import CsvFileView
from view_database import DatabaseView
from view_pickle import PickleView


if __name__ == "__main__":
    cmd_view = CommandView()
    csv_view = CsvFileView()
    pickle_view = PickleView()
    database_view = DatabaseView()
    view_list = [csv_view, database_view, pickle_view]
    # running controller function
    ctrl = Controller(view_list, cmd_view, Employee())
    # set the controller so cmd_view can call methods within the controller
    cmd_view.set_controller(ctrl)
    ctrl.start()


