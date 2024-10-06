punctuation = set(r"""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~""")
with open('text.txt') as file:
    for line_number, line in enumerate(file, start=1):
        with open('output.txt', 'a') as result:
            letters_count = sum(char.isalpha() for char in line)
            punct_count = sum(char in punctuation for char in line)
            result.write(f"Line {line_number}: {line.strip()} ({letters_count})({punct_count})\n")