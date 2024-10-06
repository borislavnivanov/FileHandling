import os


def create(file_name: str) -> None:
    with open(file_name, 'w') as file:
        file.write('')


def add(file_name: str, text: str) -> None:
    with open(file_name, 'w') as file:
        file.write(text + '\n')


def replace(file_name: str, old_str: str, new_str: str) -> None:
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        with open(file_name, 'w') as file:
            file.write(content.replace(old_str, new_str))
    except FileNotFoundError:
        print('An error occurred')

def delete(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('An error occurred')


while True:
    user_input = input()
    if user_input == 'End':
        break
    com = user_input.split('-')
    if com[0] == 'Create':
        create(com[1])
    elif com[0] == 'Add':
        add(com[1], com[2])
    elif com[0] == 'Replace':
        replace(com[1], com[2], com[3])
    elif com[0] == 'Delete':
        delete(com[1])
