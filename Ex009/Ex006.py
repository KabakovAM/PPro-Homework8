import csv
import pickle

def form_pickle_to_csv(pickle_path):
    with open(pickle_path, 'rb') as data_output:
        new_dic = dict(pickle.load(data_output))
    with open('level_up.csv', 'w', encoding='utf-8') as data_input:
        csv_write = csv.writer(data_input, lineterminator='\n', delimiter=';')
        for key_0, value_0 in new_dic.items():
            for key_1, value_1 in value_0.items():
                csv_write.writerow([key_0, key_1, value_1])

if __name__ == '__main__':
    pickle_path = 'level_up.pickle'
    form_pickle_to_csv(pickle_path)