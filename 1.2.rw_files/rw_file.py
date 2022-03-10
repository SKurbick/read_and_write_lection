# # with open('text.txt') as f:
# #     for line in f:
# #         print(line.strip())
# file = open('text.txt')
# data = file.read()
# print(data)
# file.close()

def is_closed(file_):
    if file_.closed:
        print('file is closed')
    else:
        print('file is opened')


with open('text.txt') as f:
    print(type(f))
    data = f.read()
    print(data)
    is_closed(f)
is_closed(f)
