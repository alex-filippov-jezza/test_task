from classes.checkClass import Check


file_path = 'чеки.txt'
checks = Check(file_path)
df = checks.get_data()
checks.sorted_checks_to_file()

print(df)
