# written by Vaishali

# not completed

import shelve
from view import View

class ShelveData(View):
    def __init__(self):
        pass

    def get_input(self, file_name):
        with shelve.open(file_name) as s:
            existing = s['myDict']
        return self.dict_to_list(existing)

    def save_data_to_new(self, file_name, data_list):
        with shelve.open(file_name) as my_shelfed_dict:
            my_shelfed_dict["myDict"] = self.list_to_dict(data_list)
