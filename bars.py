import json
from sys import argv


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as info_bars:
        return json.load(info_bars)


def get_biggest_bar(bars_dict):
    sorted_size_bar_list = []
    for numbers_of_bar in bars_dict_list:
        sorted_size_bar_list.append(numbers_of_bar)
    return max(sorted_size_bar_list, key=lambda
               d: d['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars_dict):
    sorted_size_bar_list = []
    for numbers_of_bar in bars_dict_list:
        sorted_size_bar_list.append(numbers_of_bar)
    return min(sorted_size_bar_list, key=lambda
               d: d['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars_dict, longitude, latitude):
    sort_close_bar_list = []
    for numbers_of_bar in bars_dict_list:
        bars_coordinates = numbers_of_bar['geometry']['coordinates']
        sort_close_bar_list.append(bars_coordinates)
    bar_dict = {}
    for num_bar in range(len(bars_dict_list)):
        sorted_coords = (sort_close_bar_list[num_bar][0] - longitude) ** 2 + \
                        (sort_close_bar_list[num_bar][1] - latitude) ** 2
        bar_dict[num_bar] = sorted_coords
        number_name = min(bar_dict, key=bar_dict.get)
    return bars_dict_list[number_name]


if __name__ == '__main__':
    try:
        bars_dict = load_data(argv[1])
        bars_dict_list = bars_dict['features']
    except UnicodeDecodeError:
        print("Необходима база данных формата json")
    print("Какую информацию по барам Москвы Вы хотите получить?"
          "\n1.Вывести самый большой бар Москвы"
          "\n2.Вывести самый маленький бар Москвы"
          "\n3.Вывести ближайший бар")
    second_question = input("")
    if second_question == "1":
        print(get_biggest_bar(bars_dict))
    elif second_question == "2":
        print(get_smallest_bar(bars_dict))
    elif second_question == "3":
        try:
            longitude = float(input("Введите долготу: "))
            latitude = float(input("Введите широту: "))
        except ValueError:
            print("Укажите целые, либо дробные числа")
        else:
            print(get_closest_bar(bars_dict, longitude, latitude))
    else:
        print("Выберите один из предложенных вариантов")
