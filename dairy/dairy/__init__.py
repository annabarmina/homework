import sys

from dairy import storage
from datetime import datetime

get_connection = lambda: storage.connect('dairy.sqlite')

def action_add():
	task_name = input('\nВнесите новую задачу')
	task_descr = input('\nВведите описание задачи')
	time_plan = input('\nВведите плановую дату выполнения')
	if task_name:
		if time_plan:
			with get_connection() as conn:
				storage.add_task(conn, task_name, task_descr, time_plan)
		else: 
			print('\nПлановое время выполнения должно быть заполнено')
			action_add()
	else: 
		print('\nНазвание задачи должно быть заполнено')
		action_add()


def action_find_all():
	with get_connection() as conn:
		tasks = storage.find_all(conn)

	template = '{task[task_name]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'
	for task in tasks:
	    print(template.format(task=task))


def action_find():
	print('''
a. По ID задачи
b. По названию
c. По статусу
d. По плановому времени завершения задачи
e. По фактическому времени завершения задачи
		''')

	points = {
	'a': action_find_id,
	'b': action_find_name,
	'c': action_find_status,
	'd': action_find_plan,
	'e': action_find_fact
	}

	cmdf = input('\nВведите номер поля для поиска: ')
	point = points.get(cmdf)
	if point:
		with get_connection() as conn:
			storage.point()
	else:
		print('Такого пункта нет в меню')

"""
def action_edit():
	edits= {
'a': action_edit_descr
'b': action_edit_time_plan
}
	cmde = input('''
a. Скорректировать описание задачи
b. Скорректировать плановое время выполнения задачи

Введите подпункт задачи: ''')
	edit = edits.get(cmde)
	if edit:
		edit()
		else:
			print('Неизвестная команда')


def action_edit_descr():
	with get_connection() as conn:
		tasks = storage.edit_descr(conn, id)

	template = '{task[task_name]} - {task[task_discr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'
	for task in tasks:
	    print(template.format(task=task))
"""


def action_edit_time_plan():
	with get_connection() as conn:
		tasks = storage.edit_time_plan(conn, id)

	template = '{task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'
	for task in tasks:
	    print(template.format(task=task))


def main():
	with get_connection() as conn:
		storage.initialize(conn)

	action_show_menu()

	actions = {
	'1': action_add,
	'2': action_find_all,
	'3': action_find,
	'4': action_edit_time_plan,
	'5': action_status_done,
	'6': action_status_returned,
	'7': action_del,
	'm': action_show_menu,
	'q': action_exit
	}

	while 1:
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		if action:
			action()
		else:
			print('Неизвестная команда')


def action_status_done():
	with get_connection() as conn:
		storage.edit_status_done(conn, id)


def action_status_returned():
	with get_connection() as conn:
		storage.edit_status_return(conn, id)

def action_del():
	cmdd = input('''
a. Удалить 1 задачу
b. Удалить все завершенные задачи

Введите номер команды:
		''')
	if cmdd == 'a':
		with get_connection() as conn:
			storage.del_task(conn, id)
	elif cmdd == 'b':
		with get_connection() as conn:
			storage.del_done(conn)
	else:
		print('Неизвестная команда')


def action_exit():
	sys.exit()


def action_show_menu():
	print('''
1. Добавить новую задачу
2. Вывести все задачи на экран
3. Найти задачу
4. Перенести плановое время исполнения задачи
5. Изменить статус задачи на "Выполнено"
6. Вернуть задачу на доработку
7. Удалить задачу
______________________________
m. Показать меню
q. Выйти
	''')





def action_find_id():
	field = input('\nВведите ID для поиска: ')
	with get_connection() as conn:
		tasks = storage.find_task_by_id(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))


def action_find_name():
	field = input('\nВведите название задачи для поиска: ')
	with get_connection() as conn:
		tasks = storage.find_task_by_name(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))


def action_find_status():
	field = input('\nВведите статус задачи для поиска: New / Done / Returned ')
	with get_connection() as conn:
		tasks = storage.find_task_by_status(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))


def action_find_created():
	field = input('\nВведите дату внесения задачи в ежедневник для поиска: ')
	with get_connection() as conn:
		tasks = storage.find_task_by_time_created(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))


def action_find_plan():
	field = input('\nВведите плановую дату выполнения задачи для поиска: ')
	with get_connection() as conn:
		tasks = storage.find_task_by_time_plan(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))


def action_find_fact():
	field = input('\nВведите фактическую дату выполнения задачи для поиска: ')
	with get_connection() as conn:
		tasks = storage.find_task_by_time_fact(conn, field)

	template = '{task[ID]} - {task[task_name]} - {task[task_descr]} - {task[time_created]} - {task[time_plan]} - {task[time_fact]} - {task[status]}'

	for task in tasks:
	    print(template.format(task=task))
