def rotate(text, key):
    list_caesar = []
    for letter in text:
        if letter.islower():
            base = ((ord(letter) - ord("a")) + key) % 26
            list_caesar.append(chr(base + ord("a")))
        elif letter.isupper():
            base = ((ord(letter) - ord("A")) + key) % 26
            list_caesar.append(chr(base + ord("A")))
        else:
            list_caesar.append(letter)
    return "".join(list_caesar)