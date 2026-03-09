vovels = "aeiou"
def disemvowel(string_: str):
	return "".join([x for x in string_ if x.lower() not in vovels])


print(disemvowel("1"))