

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def translate(text):
	if text[0] in VOWELS or text[0:2] in ["xr", "yt"]:
		return text + "ay"
	if "qu" in text:
		qu_idx = text.find("qu")
		leading_consonants = ""
		for idx in range(qu_idx):
			if text[idx] in CONSONANTS:
				leading_consonants += text[idx]
		moved_part = leading_consonants + "qu"
		remaining_part = text[len(moved_part):]
		return remaining_part + moved_part + "ay"

	if "y" in text and text[0] != "y":
		y_idx = text.find("y")
		leading_consonants = ""
		for idx in range(y_idx):
			if text[idx] in CONSONANTS:
				leading_consonants += text[idx]
		remaining_part = text[len(leading_consonants):]
		return remaining_part + "ay"
	for idx, char in enumerate(text):
		if char in VOWELS:
			return text[idx:] + text[:idx] + "ay"

	return text + "ay"




text = "pig"
print(translate(text))