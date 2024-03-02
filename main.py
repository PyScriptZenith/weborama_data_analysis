import csv
from collections import Counter

# Читаем csv - файл и записываем данные в список

with open("table.csv", encoding='utf-8') as f:
    content = csv.reader(f)
    data_csv = []
    for data in content:
        data_csv.append(data)

# Сохраняем только id в список, без хэша
data_for_analysis = []
for data in data_csv:
    data_for_analysis.append(data[1])


# Создаем объект Counter

id_count = Counter(data_for_analysis)

# Вычисляем число повторений для каждого id

most_common_id = id_count.most_common()


# Выводим только те id, которые встретились 3 раза
for id in most_common_id:
    if id[1] == 3:
        print(f'id {id[0]} встречается 3 раза')


# Выводим все id и частоту их повторений
for id in most_common_id:
    print(f"id {id[0]} встречается {id[1]} раз")

