# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

### для проверки необходимо создать папку c файлами на диске D - d:\\Python_hw\\Sem_7\\ 

import os


__all__ = ['rename_group_files', 'get_pre']


dir_path = "d:\\Python_hw\\Sem_7\\"

def rename_group_files(num_count: int, extension_old: str, extension_new: str, range_old_name: list, new_name = ""):
    num = 0
    for file_name in os.listdir(dir_path):
        part_to_save = ""
        if os.path.splitext(file_name)[1] == ('.' + extension_old):
            num += 1
            if len(os.path.splitext(file_name)[0]) >= range_old_name[1]:
                part_to_save = file_name[range_old_name[0] - 1:range_old_name[1]]
            elif len(os.path.splitext(file_name)[0]) < range_old_name[1] and len(os.path.splitext(file_name)[0]) >= range_old_name[0]:
                part_to_save = file_name[range_old_name[0] - 1:len(os.path.splitext(file_name)[0])]
            os.rename(dir_path + file_name, dir_path + part_to_save + new_name + get_pre(num_count, num) + '.' + extension_new)

def get_pre(num_cnt: int, num_current: int):
    result = str(num_current)
    for i in range(0, num_cnt - len(str(num_current))):
        result = "0" + result
    return result

if __name__ == '__main__':
    rename_group_files(5, 'zip', 'bin', [8, 17], "qwerty")