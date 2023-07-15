import csv
import pickle

def form_csv_to_pickle(csv_path):
    level_dic = {}
    with open(csv_path, 'r', encoding='utf-8') as data_output:
        csv_read = csv.reader(data_output, lineterminator='\n', delimiter=';')
        for line in csv_read:
            if not line[0] in level_dic:
                level_dic[line[0]] = {}
            new_line = str(line[2][1:-1]).split(',')
            new_line[0]=new_line[0][1:-1]
            level_dic[line[0]][line[1]] = new_line
    res = pickle.dumps(level_dic)
    print(res)


if __name__ == '__main__':
    csv_path = 'level_up.csv'
    form_csv_to_pickle(csv_path)