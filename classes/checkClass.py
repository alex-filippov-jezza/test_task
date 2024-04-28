import pandas as pd
import os


class Check:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def get_data(self):
        data = []
        with open(self.file_path, 'r') as file:

            for line in file:
                parts = line.strip().split('_')
                month = parts[-1].split('.')[0]
                service = '_'.join(parts[:-1])
                data.append([month, service])

        return pd.DataFrame(data, columns=['Месяц', 'Услуга'])
