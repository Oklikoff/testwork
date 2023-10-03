import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Загрузка списка ФИО из CSV файла
fio_list = []
with open('fio.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        fio_list.append(row[0])

# Инициализация WebDriver
driver = webdriver.Chrome()

# Открытие страницы поиска сертификатов
driver.get("https://www.megaputer.ru/produkti/sertifikat/")
time.sleep(5)

# Поиск сертификатов по каждой ФИО
results = []

for fio in fio_list:
    # Ввод фамилии в поле поиска
    search_field = driver.find_element(By.ID, 'certificates-text')
    search_field.clear()  # Очистка поля ввода, если в нем есть предыдущий запрос
    search_field.send_keys(fio)
    time.sleep(2)  # Сокращение времени ожидания для повышения производительности

    # Нажатие кнопки "Поиск"
    search_btn = driver.find_element(By.ID, 'certificates-button')
    search_btn.click()
    time.sleep(5)

    # Сбор информации о найденных сертификатах
    certs = []

    elements = driver.find_elements(By.TAG_NAME, "td")

    for el in elements:
        title = el.text
        certs.append(title)

    result = certs[1:]

    data = []
    for i in range(0, len(result), 2):
        data.append(result[i:i + 2])
    # print(result)

    # Добавление результатов поиска
    results.append(f"{fio}, " + ", ".join(result))

# Выход из браузера
driver.quit()

# Запись результатов в CSV-файл
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['ФИО', 'Сертификат', 'Дата выдачи']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for certs in results:
        certs = certs.split(', ')
        fio = certs[0]
        for i in range(1, len(certs), 2):
            if i + 1 < len(certs):
                writer.writerow({'ФИО': fio, 'Сертификат': certs[i], 'Дата выдачи': certs[i + 1]})
            else:
                writer.writerow({'ФИО': fio})
