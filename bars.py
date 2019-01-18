# -*- coding: utf8 -*-
import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fh:
        return(json.load(fh))


def get_biggest_bar(data):
    list1=[]
    x = 0
    while x <= (len(data['features'])-1):
    	с = data['features'][x]['properties']['Attributes']
    	list1.append(с.copy())
    	x+=1
    return(max(list1,key= lambda d: d['SeatsCount']).get('Name'))


def get_smallest_bar(data):
    list1=[]
    x = 0
    while x <= (len(data['features'])-1):
    	с = data['features'][x]['properties']['Attributes']
    	list1.append(с.copy())
    	x+=1
    return(min(list1,key= lambda d: d['SeatsCount']).get('Name'))


def get_closest_bar(data, longitude, latitude):
    list2=[]
    x = 0
    while x <= (len(data['features'])-1):
    	d = data['features'][x]['geometry']['coordinates']
    	list2.append(d.copy())
    	x+=1
    e = {}
    n = []
    v = 0
    while v <= (len(data['features'])-1):
    	n = [(list2[v][0]-longitude)**2+(list2[v][1]-latitude)**2]
    	c = data['features'][v]['properties']['Attributes']['Name']
    	e[c] = n
    	v+=1 
    return(min(e, key=e.get))

if __name__ == '__main__':
    h = input("Введите месторасположение файла")
    g = load_data(h)
    print("Какую информацию по барам Москвы Вы хотите получить?\n1.Вывести самый большой бар Москвы\n2.Вывести самый маленький бар Москвы\n3.Вывести ближайший бар")	
    u = input("")
    if u == "1":
        print(get_biggest_bar(g))	
    elif u == "2":
	    print(get_smallest_bar(g))
    elif u == "3":
        longitude = float(input("Введите долготу"))
        latitude = float(input("Введите широту"))
        print(get_closest_bar(g, longitude, latitude))
    			