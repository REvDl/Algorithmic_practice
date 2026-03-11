vovels = "аоуеиіыэяюєї"
def CountVovels(text:str) -> str:
	count = 0
	for i in text:
		if i.lower() in vovels:
			count += 1
	print(count)
	return "Голосних більше" if count > len(text) - count else "Приголосних більше"


print(CountVovels("ааа"))