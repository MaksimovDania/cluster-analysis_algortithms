import numpy as np


class FileReader:
    @staticmethod
    def read_file(filename):
        data = np.loadtxt(filename)
        return data
