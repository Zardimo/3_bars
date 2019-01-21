# -*- coding: utf8 -*-
import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fh:
        return json.load(fh)


def get_biggest_bar(data):
    sorted_size_bar_list=[]
    x = 0
    while x <= (len(data['features'])-1):
    	bar_list = data['features'][x]['properties']['Attributes']
    	sorted_size_bar_list.append(bar_list.copy())
    	x+=1
    return max(sorted_size_bar_list, key= lambda d: d['SeatsCount']).get('Name')


def get_smallest_bar(data):
    sorted_size_bar_list=[]
    x = 0
    while x <= (len(data['features'])-1):
    	bar_list = data['features'][x]['properties']['Attributes']
    	sorted_size_bar_list.append(bar_list.copy())
    	x+=1
    return min(sorted_size_bar_list, key= lambda d: d['SeatsCount']).get('Name')


def get_closest_bar(data, longitude, latitude):
    sorted_close_bar_list=[]
    x = 0
    while x <= (len(data['features'])-1):
    	bars_coordinates = data['features'][x]['geometry']['coordinates']
    	sorted_close_bar_list.append(bars_coordinates.copy())
    	x+=1
    bar_dict = {}
    sorted_coordinates_list = []
    v = 0
    while v <= (len(data['features'])-1):
    	sorted_coordinates_list = [(sorted_close_bar_list[v][0]-longitude)**2+(sorted_close_bar_list[v][1]-latitude)**2]
    	bar_name = data['features'][v]['properties']['Attributes']['Name']
    	bar_dict[bar_name] = sorted_coordinates_list
    	v+=1 
    return min(bar_dict, key=bar_dict.get)

if __name__ == '__main__':
    first_question = input("Введите месторасположение файла")
    data_bank = load_data(first_question)
    print("Какую информацию по барам Москвы Вы хотите получить?\n1.Вывести самый большой бар Москвы\n2.Вывести самый маленький бар Москвы\n3.Вывести ближайший бар")	
    second_question = input("")
    if second_question == "1":
        print(get_biggest_bar(data_bank))	
    elif second_question == "2":
	    print(get_smallest_bar(data_bank))
    elif second_question == "3":
        longitude = float(input("Введите долготу"))
        latitude = float(input("Введите широту"))
        print(get_closest_bar(data_bank, longitude, latitude))