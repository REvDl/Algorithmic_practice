def find_ball(scales):
	low = 0
	high = 7
	while low < high:
		mid = (low + high) // 2
		left_balls = list(range(low, mid + 1))
		right_balls = list(range(mid + 1, high + 1))
		res = scales.get_weight(left_balls, right_balls)
		if res == -1:
			high = mid
		else:
			low = mid + 1
	return low
