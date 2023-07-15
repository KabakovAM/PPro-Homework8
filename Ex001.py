import json


def from_txt_to_json():
    temp = []
    with (
        open ('nam_and_num.txt', 'r',encoding='utf-8') as data_output,
        open ('nam_and_num.json', 'a') as data_input
    ):
        for line in data_output:
            temp.append(line[:-2].capitalize())
        json.dump(temp, data_input, indent= 4)


if __name__ == '__main__':
    from_txt_to_json()