# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

__all__ = ['save_in_json', 'save_in_csv', 'save_in_pickle', 'get_dir_size', 'get_size', 'get_dir_info']

from pathlib import Path
import csv
import json
import pickle
import os

def save_in_json(json_data: json):
    with open('file_1.json', 'w') as f:
        json.dump(json_data, f, indent=2)

def save_in_csv(rows: list):
    with open ('file_2.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['name', 'path', 'size', 'file_or_dir'], dialect = 'excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(rows)

def save_in_pickle(json_data: json):
    with open ('file_3.pickle', 'wb') as f:
        pickle.dump(f'{pickle.dumps(json_data)}', f)

def get_dir_size(path='.'):
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result

def get_size(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)

def get_dir_info(path: Path):
    json_data = {}
    rows = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            size = get_size(dirpath + '/' + dir)
            json_data.setdefault(dirpath, {})
            json_data[dirpath].update({dir: {'size': size, 'file_or_dir': 'directory'}})
            rows.append({'name': dir, 'path': dirpath, 'size': size, 'file_or_dir': 'directory'})
        for fn in filenames:
            size = get_size(dirpath + '/' + fn)
            json_data.setdefault(dirpath, {})
            json_data[dirpath].update({fn: {'size': size, 'file_or_dir': 'file'}})
            rows.append({'name': fn, 'path': dirpath, 'size': size, 'file_or_dir': 'file'})
    save_in_json(json_data)
    save_in_csv(rows)
    save_in_pickle(json_data)

if __name__ == "__main__":
    dir_to_check = "C:\\temp\\"
    get_dir_info(dir_to_check)