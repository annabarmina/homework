def get_quadrant_number(x, y):
	if x == 0 or y == 0:
		raise ValueError
	if x > 0:
		if y > 0:
			return(1)
		else:
			return(4)
	else:
		if y > 0:
			return(2)
		else:
			return(3)