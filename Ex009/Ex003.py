import csv
import json


def form_json_to_csv():
    with open ('level.json', 'r', encoding='utf-8') as data_output:
        level_dic = json.load(data_output)
    with open ('level.csv', 'w', encoding='utf-8') as data_input:
        csv_write = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for key_0, value_0 in level_dic.items():
            for key_1, value_1 in value_0.items():
                csv_write.writerow([key_0, key_1, value_1])


if __name__ == '__main__':
    form_json_to_csv()