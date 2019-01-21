# -*- coding: utf8 -*-
import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fh:
        return json.load(fh)


def get_biggest_bar(bars_dict):
    sorted_size_bar_list = []
    for item in range(len(bars_dict['features']) - 1):
        bar_list = bars_dict['features'][item]['properties']['Attributes']
        sorted_size_bar_list.append(bar_list.copy())
    return max(sorted_size_bar_list, key=lambda d: d['SeatsCount']).get('Name')


def get_smallest_bar(bars_dict):
    sorted_size_bar_list = []
    for item in range(len(bars_dict['features']) - 1):
        bar_list = bars_dict['features'][item]['properties']['Attributes']
        sorted_size_bar_list.append(bar_list.copy())
    return min(sorted_size_bar_list, key=lambda d: d['SeatsCount']).get('Name')


def get_closest_bar(bars_dict, longitude, latitude):
    sorted_close_bar_list = []
    for item in range(len(bars_dict['features']) - 1):
        bars_coordinates = bars_dict['features'][item]['geometry']['coordinates']
        sorted_close_bar_list.append(bars_coordinates)
    bar_dict = {}
    for item in range(len(bars_dict['features'])-1):
        sorted_coords = (sorted_close_bar_list[item][0] - longitude) ** 2 + \
                        (sorted_close_bar_list[item][1] - latitude) ** 2
        bar_name = bars_dict['features'][item]['properties']['Attributes']['Name']
        bar_dict[bar_name] = sorted_coords
    return min(bar_dict, key=bar_dict.get)


if __name__ == '__main__':
    first_question = input("Введите месторасположение файла: ")
    bars_dict = load_data(first_question)
    print("Какую информацию по барам Москвы Вы хотите получить?  \
    \n1.Вывести самый большой бар Москвы  \
    \n2.Вывести самый маленький бар Москвы\n3.Вывести ближайший бар")
    second_question = input("")
    if second_question == "1":
        print(get_biggest_bar(bars_dict))
    elif second_question == "2":
        print(get_smallest_bar(bars_dict))
    elif second_question == "3":
        longitude = float(input("Введите долготу: "))
        latitude = float(input("Введите широту: "))
        print(get_closest_bar(bars_dict, longitude, latitude))
