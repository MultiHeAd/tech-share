data_list = [
    '123.mp4',
    '456.mp4'
]

for i in range(len(data_list)):
    data_list[i] = data_list[i].replace('.mp4', '')

print(data_list)