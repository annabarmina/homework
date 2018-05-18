def get_free_land(uch, gr):
	if uch[0] == 0:
		raise ValueError("Не задана площадь участка")
	elif gr[0] == 0 or gr[1] == 0:
		raise ValueError('Не задана площадь грядки')
	elif uch[0]*100 <= gr[0] * gr[1]:
		raise ValueError('Размер грядки больше размера участка')
	else:
		return uch[0] * 100 % (gr[0] * gr[1])

#print(get_free_land([0, "1:1"], [15, 25]))
# python task_exception_free_land.py