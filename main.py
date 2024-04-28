from classes.checkClass import Check


file_path = 'res/чеки.txt'
checks = Check(file_path)
checks.sorted_checks_to_file()
checks.add_unpaid_services()

