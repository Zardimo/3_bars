import json
import os
from sys import argv


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Неверно указан путь файла")
        raise SystemExit
    with open(filepath, "r", encoding="utf-8") as info_bars:
        return json.load(info_bars)


def get_biggest_bar(bars):
    return max(bars, key=lambda
               d: d["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars):
    return min(bars, key=lambda
               d: d["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(bars):
    longitude = float(input("Введите долготу: "))
    latitude = float(input("Введите широту: "))
    number_name = min(bars, key=lambda
                      x: coords(x["geometry"]["coordinates"][0], longitude,
                                x["geometry"]["coordinates"][1], latitude))
    return number_name


def coords(x, x1, y, y1):
    delta_x = (x-x1)**2
    delta_y = (y-y1)**2
    return delta_x+delta_y


if __name__ == "__main__":
    try:
        bars = load_data(argv[1])["features"]
        longitude = 0
        latitude = 0
        print("Какую информацию по барам Москвы Вы хотите получить?"
              "\n1.Вывести самый большой бар Москвы"
              "\n2.Вывести самый маленький бар Москвы"
              "\n3.Вывести ближайший бар")
        second_question = int(input('Выберите опцию: '))
        map = {
            1: get_biggest_bar,
            2: get_smallest_bar,
            3: get_closest_bar
        }
        print(map[second_question](bars)["properties"]["Attributes"]["Name"])
    except IndexError:
        print("Укажите верный путь к файлу")
    except ValueError:
        print("Укажите целые, либо дробные числа")
