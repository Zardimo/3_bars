import json
import os
from sys import argv


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file_bars:
            return json.load(file_bars)


def get_biggest_bar(bars):
    return max(bars["features"], key=lambda
               d: d["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars):
    return min(bars["features"], key=lambda
               d: d["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(bars):
    number_name = min(bars["features"], key=lambda
                      x: calculate_coords(x["geometry"]["coordinates"][0],
                      longitude,
                      x["geometry"]["coordinates"][1],
                      latitude))
    return number_name


def calculate_coords(x, x1, y, y1):
    delta_x = (x-x1)**2
    delta_y = (y-y1)**2
    return delta_x+delta_y


if __name__ == "__main__":
    try:
        bars = load_data(argv[1])
    except IndexError:
        print("Укажите путь к файлу")
        raise SystemExit
    if bars is None:
        print("Укажите верный путь к файлу")
        raise SystemExit
    option_map = {
        "1": get_biggest_bar,
        "2": get_smallest_bar,
        "3": get_closest_bar
    }
    print("Какую информацию по барам Москвы Вы хотите получить?"
          "\n1.Вывести самый большой бар Москвы"
          "\n2.Вывести самый маленький бар Москвы"
          "\n3.Вывести ближайший бар")
    question = input("Выберите опцию: ")
    try:
        if question == "3":
            longitude = float(input("Введите долготу: "))
            latitude = float(input("Введите широту: "))
        print(option_map[question](bars)["properties"]["Attributes"]["Name"])
    except ValueError:
        print("Укажите целые, либо дробные числа")
