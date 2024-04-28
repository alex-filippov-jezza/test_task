from classes.checkClass import Check


file_path = 'чеки.txt.'

# Создаем экземпляр класса DataProcessor
checks = Check(file_path)

# Обрабатываем данные
df = checks.get_data()

# Выводим DataFrame
print(df)
