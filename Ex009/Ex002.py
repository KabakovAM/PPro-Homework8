import json


def name_level_id():
    level_dic = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}  
    name = input('Введите имя: ')
    n_id = input('Введите личный идентификатор: ')
    level = input('Введите уровень доступа: ')
    with open ('level.json', 'r', encoding='utf-8') as data_output:
        level_dic = json.load(data_output)
    for key, value in level_dic.items():
        if n_id in level_dic[key]:
            print('Введён неправильный идентификатор.')
            return name_level_id()
    if level in level_dic:
        level_dic[level][n_id] = name
    else:
        print('Введён неправильный уровень доступа.')
        return name_level_id()
    with open ('level.json', 'w') as data_input:
        json.dump(level_dic, data_input, indent=4)


if __name__ == '__main__':
    for _ in range(10):
        name_level_id()