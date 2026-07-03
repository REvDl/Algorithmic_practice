

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def translate_word(text:str) -> str:
	if text[0] in VOWELS or text[0:2] in ["xr", "yt"]:
		return text + "ay"
	if "qu" in text:
		qu_idx = text.find("qu")
		if all(char not in VOWELS for char in text[:qu_idx]):
			return text[qu_idx + 2:] + text[:qu_idx + 2] + "ay"
	if "y" in text and text[0] != "y":
		y_idx = text.find("y")
		if all(char not in VOWELS for char in text[:y_idx]):
			return text[y_idx:] + text[:y_idx] + "ay"
	for idx, char in enumerate(text):
		if char in VOWELS:
			return text[idx:] + text[:idx] + "ay"
	return text + "ay"


def translate(text):
    return " ".join(translate_word(w) for w in text.split())



text = "pig"
print(translate(text))