import csv
import pickle
import json
import os

def recursion_folder(csv_path):
    file_data = []
    folder_data = []
    temp = []
    for a, b, c in os.walk(csv_path):
        data_size = 0
        folder_list = a.split('\\')
        for i in c:
            file_path = ('{}\\{}'.format(a, i))
            temp = ['Файл:', i, 'Родительская папка:', *folder_list[-1:], 'Размер файла:', os.path.getsize(file_path)]
            data_size += os.path.getsize(file_path)
            file_data.append(temp.copy())
            temp.clear()
        temp = ['Папка:', *folder_list[-1:], 'Родительская папка:', *folder_list[-2:-1], 'Размер вложеных файлов:', data_size]
        folder_data.append(temp.copy())
        temp.clear()
    print(len(folder_data) - 1)
    for i in range(len(folder_data) - 1 , -1, -1):
        for k in range(len(folder_data) - 1, -1, -1):
            if folder_data[i][3] == folder_data[k][1]:
                folder_data[k][5] += folder_data[i][5]
    folder_data.extend(file_data)
    with (
        open ('recursion_folder.csv', 'w',encoding='utf-8') as data_input_csv,
        open ('recursion_folder.pickle', 'wb') as data_input_pickle,
        open ('recursion_folder.json', 'w') as data_input_json
    ):
        csv_write = csv.writer(data_input_csv, lineterminator='\n', delimiter=';')
        csv_write.writerows(folder_data)
        pickle.dump(folder_data, data_input_pickle)
        json.dump(folder_data, data_input_json, indent= 4)

if __name__ == '__main__':
    folder = 'C:\\Users\\kabaa\\Desktop\\Файлы'
    recursion_folder(folder)