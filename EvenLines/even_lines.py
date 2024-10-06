lines = []
with open('text.txt') as file:
    for line_num, line in enumerate(file):
        if line_num % 2 != 0:
            continue
        for char in {"-", ",", ".", "!", "?"}:
            line = line.replace(char, '@')
        line = line.split()
        print(' '.join(reversed(line)))
