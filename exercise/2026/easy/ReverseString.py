def reverse(text):
	left, right = 0, len(text) - 1
	chars = list(text)
	while left < right:
		chars[left], chars[right] = chars[right], chars[left]
		left += 1
		right -= 1
	return "".join(chars)


print(reverse("revdi"))