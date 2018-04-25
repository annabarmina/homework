def bubble_sort(lst): 
	for i in range(len(lst)-1):              # Повторяем столько раз, сколько элементов в списке
		for i in range(len(lst)-1):      # Для каждого элемента
			if lst[i] > lst[i+1]:	 # Сравниваем элемент со следующим, и если он больше, то
				lst[i], lst[i+1] = lst[i+1], lst[i] # меняем местами
	return(lst) 
