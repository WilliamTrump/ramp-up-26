def series_resistance(lst):
	total = 0
	for item in lst:
		total += item
	if total <= 1:
		return str(total) + " ohm"
	else:
		return str(total) + " ohms"