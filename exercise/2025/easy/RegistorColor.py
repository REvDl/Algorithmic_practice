COLORS_CODE = {"black": 0, "brown":1, "red":2,
                "orange":3, "yellow":4, "green":5,
                "blue":6,"violet":7,"grey":8,"white":9 }
def value(colors):
    two_words = colors[:2]
    dict_list = []
    for i in two_words:
        color_index = COLORS_CODE.get(i, None)
        dict_list.append(color_index)
    if None in dict_list:
        return None
    return int("".join(str(item) for item in dict_list))