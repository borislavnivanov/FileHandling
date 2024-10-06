import os

files = os.listdir('./')

grouped_files = {}

for file in files:
    file_name, ext = file.split('.')
    ext = '.'+ ext.lower()
    if ext in grouped_files.keys():
        grouped_files[ext].append(file_name)
    else:
        grouped_files[ext] = [file_name]

sorted_key = sorted(grouped_files.keys())


with open('report.txt', 'a') as output:
    for key in sorted_key:
        output.write(f'{key}\n')
        for value in grouped_files[key]:
            output.write(f'---{value}\n')
