def end_corona(recovers, new_cases, active_cases):
	counter = 0
	while active_cases > 0:
		active_cases += (new_cases - recovers)
		counter += 1
	return counter