def sum_odd_and_even(lst):
	odds = 0
	evens = 0
	for item in lst:
		if item % 2 == 0:
			evens += item
		else:
			odds += item
	totals = [evens,odds]
	return totals