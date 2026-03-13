

password_variants = [
    "...randomsa",
    "...randomsA",
    "...randomsa2",
    "...randomsA2",
    "...randomsa54321",
    "...randomsA54321",
    "...arandomsa",
    "...arandomsA",
    "...arandomsa2",
    "...arandomsA2",
    "...arandomsa54321",
    "...arandoms....."
]
cursor = True
while cursor:
	for i in range(len(password_variants) -1, -1, -1):
		a = input(f"Password {password_variants[i].replace("randoms", "...")} valide? (Y/n) ")
		if a.lower() == "y":
			print("Password selected.")
			cursor = False
			break
		elif a.lower() == "n":
			password_variants.pop(i)
	print("Password not selected.")
	break