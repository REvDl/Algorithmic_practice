


def SOLVIT_Discount():
	"""
	SELECT(
		ROUND(
			COUNT(promocode_id) * 100 / COUNT(*), 2)
	) as promo_orders_percentage
	FROM orders;
	"""