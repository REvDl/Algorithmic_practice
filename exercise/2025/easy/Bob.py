def response(hey_bob):
	if not hey_bob.strip():
		return "Fine. Be that way!"

	stripped_phrase = hey_bob.strip()

	contains_letters = any(c.isalpha() for c in stripped_phrase)
	if stripped_phrase.endswith("?") and stripped_phrase.isupper() and contains_letters:
		return "Calm down, I know what I'm doing!"

	if stripped_phrase.isupper() and contains_letters:
		return "Whoa, chill out!"

	if stripped_phrase.endswith("?"):
		return "Sure."

	else:
		return 'Whatever.'