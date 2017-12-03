# written by Vaishali

from cmd import Cmd


class CommandView(Cmd):
    """
    Uses the Cmd class to provide framework to write line-orientated classes
    """

    def __init__(self):
        """
        Calls the super class constructor
        """
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "unknown"
        self.controller = None

    def set_controller(self, controller):
        """
        Controller initialised ready for calling methods within the controller
        :controller:
        :return:
        """
        self.controller = controller

    def do_read(self, file_name):
        """
        Reads data from a file
        Syntax: read [the_name]
        :file_name: valid extensions .db(SQLite) .csv .pickle
        """
        if file_name:
            self.controller.open_file_and_validate(file_name)
        else:
            print("Usage: read <file_name>")

    def do_show(self, file_name):
        """
        Shows either the records of the file previously input using <read>
        or if given the records in the <file_name> parameter
        Syntax: show or show <file_name>
        """
        if file_name:
             self.controller.open_file_and_validate(file_name)
        else:
            print("Records shown are from the "
                  "file inputted using \'read <filename>\'")
        self.controller.show_records()

    def do_graph(self, input_line):
        """
        Graphs out the Male to Female ratio of the records in the file
        Syntax: graph <file_name> [graph_type]
        :file_name:
        :argument graph_type: <pie> default: bar
        :return:
        """
        if input_line:
            split_array = self.split_input_line(input_line)
            self.controller.show_graph(split_array[0], split_array[1])
        else:
            print("Usage: graph <filename> [args]")

    def split_input_line(self, input_line):
        split_array = []
        # split up the file_name string to get the arguments
        args = input_line.split()
        split_array.append(args[0])
        if len(args) > 1:
            split_array.append(args[1])
        else:
            split_array.append("")
        return split_array

    def do_save(self, file_name):
        """
        Saves the file to new file name
        Syntax: save <file_name>
        :file_name: valid extensions .db .csv .pickle
        """
        # result = False
        if file_name:
            result = self.controller.save_data_to_new_file(file_name)
            return True
        else:
            print("Usage: save <file_name>")
            return False

    @staticmethod
    def do_quit(line):
        """
        Quit from the program
        Syntax: quit or q
        """
        print("Quitting .......")
        return True

    # shortcuts
    do_q = do_quit
