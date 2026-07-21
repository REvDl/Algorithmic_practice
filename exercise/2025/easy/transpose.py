from itertools import zip_longest

def transpose(text):
    result = []
    lines = text.split("\n")
    rows = zip_longest(*lines, fillvalue = None)
    for row in rows:
        line = ""
        row_list = list(row)
        while row_list and row_list[-1] is None:
            row_list.pop()

        line = "".join(char if char is not None else " " for char in row_list)
        result.append(line)
    return "\n".join(result)
