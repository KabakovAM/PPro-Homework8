import csv
import json

def form_csv_to_json(csv_path, json_path):
    level_dic = {}
    with open(csv_path, 'r', encoding='utf-8') as data_output:
        csv_read = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in csv_read:
            if not line[0] in level_dic:
                level_dic[line[0]] = {}
            new_line = ('{}{}'.format('0'*abs(len(line[1])-10), line[1]))
            level_dic[line[0]][new_line] = (line[2].capitalize(), hash(line[2] + line[1]))
    with open (json_path, 'a') as data_input:
        json.dump(level_dic, data_input, indent=4)

if __name__ == '__main__':
    csv_path = 'level.csv'
    json_path = 'level_up.json'
    form_csv_to_json(csv_path, json_path)
