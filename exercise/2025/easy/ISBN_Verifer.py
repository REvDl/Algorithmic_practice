def is_valid(isbn):
	cleaned = isbn.replace("-", "")
	if len(cleaned) != 10:
		return False
	for i in range(9):
		if not cleaned[i].isdigit():
			return False
	if cleaned[9] not in "0123456789X":
		return False
	total = 0
	for i in range(9):
		total += int(cleaned[i]) * (10 - i)
	if cleaned[9] == 'X':
		total += 10
	else:
		total += int(cleaned[9])

	return total % 11 == 0