# created by Vaishali

from data_serial import DataSerial


class DataCSV(DataSerial):
    """
    Used by employee.py to return the data for a record
    """
    def unpack_data(self, record_num):
        return self._data[record_num]

    def pack_data(self):
        pass