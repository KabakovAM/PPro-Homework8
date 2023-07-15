import pickle
import json
import os


def form_json_to_pickle(folder):
    os.chdir(folder)
    list_dir = os.listdir(folder)
    for i in range(len(list_dir)):
        if list_dir[i][-4:] == 'json':
            with open (list_dir[i], 'r', encoding='utf-8') as data_output:
                data_dic = json.load(data_output)
            new_file = ('{}{}').format(list_dir[i][:-4], 'pickle')
            with open (new_file, 'wb') as data_input:
                pickle.dump(data_dic, data_input)


if __name__ == '__main__':
    folder = 'C:\\Users\\kabaa\\Desktop\\Python\\Python_pro'
    form_json_to_pickle(folder)