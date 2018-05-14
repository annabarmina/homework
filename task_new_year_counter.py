from datetime import datetime, date, timedelta

now = datetime.today()
#now = datetime(2018, 12,17, 12, 46, 5)
ny = datetime(int(now.year)+1, 1, 1)
delta = ny - now
days = delta.days
hours = delta.seconds // 3600
minuts = delta.seconds % 3600 // 60

l = [days, hours, minuts]

words1 = [['день', 'дня', 'дней'], ['час', 'часа', 'часов'], ['минута', 'минуты', 'минут']]

def counter():
	answer = ''
	for ind, n in enumerate(l):
		answer += str(l[ind])+' '
		if n % 10 == 1 and not n % 100 == 11:
			answer += str(words1[ind][0])+' '
		elif n % 10 in range(2,4) and not n%100 in range(12,14):
			answer += str(words1[ind][1])+' '
		else:
			answer += str(words1[ind][2])+' '
	return answer
'''
python task_new_year_counter.py
'''