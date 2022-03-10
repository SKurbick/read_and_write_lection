import os

fs = ['1.txt', '2.txt', '3.txt']


def read_files(files):
    all_files = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as lines:
            datas = []
            count = len(lines.readlines())
            datas.append(file)
            datas.append(count)
            with open(file, 'r', encoding='utf-8') as lined:
                datas.append(lined.read())
                all_files.append(datas)
    all_files.sort(key=lambda x: x[1])
    for data in all_files:
        for line in data:
            print(line)


read_files(fs)
