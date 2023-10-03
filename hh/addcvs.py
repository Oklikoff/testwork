import csv

# Данные для записи в CSV файл
data = ["Иванова Алена Андреевна", "Петров Михаил Викторович", "Сидоров Петр Геннадиевич"]

# Имя файла
file_name = "fio.csv"

# Запись данных в CSV файл
with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for item in data:
        writer.writerow([item])
