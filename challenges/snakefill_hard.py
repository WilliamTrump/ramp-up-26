def snakefill(n):
	board = n * n
	length = 1
	counter = 0
	while length * 2 <= board:
		counter += 1
		length = length * 2
	return counter