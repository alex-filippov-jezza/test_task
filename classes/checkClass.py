import pandas as pd
import os


class Check:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def get_data(self):
        data = []
        with open(self.file_path, 'r', encoding='utf-8-sig') as file:

            for line in file:
                parts = line.strip().split('_')
                month = parts[-1].split('.')[0]
                service = '_'.join(parts[:-1])
                data.append([month, service])
            self.df = pd.DataFrame(data, columns=['Месяц', 'Услуга'])

            month_to_number = {
                'январь': 1,
                'февраль': 2,
                'март': 3,
                'апрель': 4,
                'май': 5,
                'июнь': 6,
                'июль': 7,
                'август': 8,
                'сентябрь': 9,
                'октябрь': 10,
                'ноябрь': 11,
                'декабрь': 12
            }

            self.df['Номера'] = self.df['Месяц'].map(month_to_number)
            self.df = self.df.sort_values(by='Номера').reset_index(drop=True)
            self.df.pop('Номера')
        return self.df

    def sorted_checks_to_file(self):
        with open('new.txt', 'w', encoding='utf-8') as file:
            for index, row in self.get_data().iterrows():
                month = row['Месяц']
                service = row['Услуга']
                file.write(f"{month}/{service}_{month}.pdf\n")
