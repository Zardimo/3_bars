import json
import os
import sys
from sys import argv


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as file_bars:
        return json.load(file_bars)


def get_biggest_bar(bars):
    return max(
        bars,
        key=lambda d: d["properties"]["Attributes"]["SeatsCount"]
    )


def get_smallest_bar(bars):
    return min(
        bars,
        key=lambda d: d["properties"]["Attributes"]["SeatsCount"]
    )


def get_closest_bar(bars, longitude, latitude):
    number_name = min(
        bars,
        key=lambda x: calculate_coords(
            x["geometry"]["coordinates"][0],
            longitude,
            x["geometry"]["coordinates"][1],
            latitude
        )
    )
    return number_name


def calculate_coords(x, x1, y, y1):
    delta_x = (x-x1)**2
    delta_y = (y-y1)**2
    return delta_x+delta_y


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        exit("Укажите путь к файлу")
    try:
        bars_dict = load_data(argv[1])
    except ValueError:
        exit("Укажите верный файл")
    if not bars_dict:
        exit("Укажите верный путь к файлу")
    bars = bars_dict["features"]
    print("Самый большой бар: {}".format(
        get_biggest_bar(bars)["properties"]["Attributes"]["Name"]))
    print("Самый маленький бар: {}".format(
        get_smallest_bar(bars)["properties"]["Attributes"]["Name"]))
    print("Для нахождения ближайшего бара необходимо ввести координаты")
    try:
        print("Ближайший бар: {}".format(
            get_closest_bar(
                bars,
                float(input("Введите долготу: ")),
                float(input("Введите широту: ")))["properties"]["Attributes"]["Name"]
             )
        )
    except ValueError:
        print("Укажите целые, либо дробные числа")
