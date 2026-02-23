def equilateral(sides):
	if len(sides) == 3 and all(x > 0 and sides[0] == x for x in sides):
		return True
	return False


def isosceles(sides):
	if len(sides) != 3:
		return False
	sorted_sides = sorted(sides)
	a, b, c = sorted_sides[0], sorted_sides[1], sorted_sides[2]
	is_valid_triangle_base = (a > 0 and a + b > c)
	has_at_least_two_equal_sides = (a == b or b == c)
	if is_valid_triangle_base and has_at_least_two_equal_sides:
		return True
	else:
		return False


def scalene(sides):
	if len(sides) != 3:
		return False
	sorted_sides = sorted(sides)
	a, b, c = sorted_sides[0], sorted_sides[1], sorted_sides[2]
	if a > 0 and (a + b > c) and (len(set(sides)) == 3):
		return True
	else:
		return False
