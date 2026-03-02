import random


def count_points(points_list: list[int], n:int) -> float | int:
	points = sum(points_list)
	bonus_points = random.randint(10, 50)
	return round((n / ((points * 30) + bonus_points)) / 12, 2)


points_month = [10, 1]
sum_for_present = 7200
print(count_points(points_month, sum_for_present))
