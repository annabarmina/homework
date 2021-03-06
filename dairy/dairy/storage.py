import os.path as Path
import sqlite3


SQL_INSERT_TASK = 'INSERT INTO dairy (task_name, task_descr, time_plan) VALUES (?, ?, ?)'

SQL_UPDATE_TASK_PLAN_TIME = '''
	UPDATE dairy SET time_plan=? WHERE id=?
'''
SQL_UPDATE_TASK_DESCR = '''
	UPDATE dairy SET task_descr=? WHERE id=?
'''

SQL_FINISH_TASK = '''
	UPDATE dairy SET time_fact=CURRENT_DATE, status='Done' WHERE id=?
'''

SQL_RETURN_TASK = '''
	UPDATE dairy SET time_fact='', status='Returned' WHERE id=?
'''

SQL_SELECT_ALL = '''
	SELECT 
        id, task_name, time_created, time_plan, time_fact, status   
    FROM 
        dairy
'''
SQL_SELECT_TASK_BY_ID = SQL_SELECT_ALL + 'WHERE id=?'

SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + 'WHERE status=?'

SQL_SELECT_TASK_BY_NAME = SQL_SELECT_ALL + 'WHERE task_name=?'

SQL_SELECT_TASK_BY_TIME_CREATED = SQL_SELECT_ALL + 'WHERE time_created=?'

SQL_SELECT_TASK_BY_TIME_PLAN = SQL_SELECT_ALL + 'WHERE time_plan=?'

SQL_SELECT_TASK_BY_TIME_FACT = SQL_SELECT_ALL + 'WHERE time_fact=?'

SQL_DELETE_TASK = 'DELETE FROM dairy WHERE id=?'

SQL_DELETE_DONE = 'DELETE FROM dairy WHERE status="Done"'

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]

	return d


def connect(db_name=None):
	""" Выполняет подключение к БД"""
	if db_name is None:
		db_name = ':memory:'  

	conn = sqlite3.connect(db_name)
	conn.row_factory = dict_factory
	
	return conn


# Инициализация БД
def initialize(conn):
	script_path = Path.join(Path.dirname(__file__), 'bd.sql')

	with conn, open(script_path) as f:
		conn.executescript(f.read())

""" добавить задачу в базу """
def add_task(conn, task_name, task_descr, time_plan):
	'''
	if not task_name:
		raise RuntimeError("Название задачи должно быть заполнено")
	if not time_plan:
		raise RuntimeError("Плановое время выполнения должно быть заполнено")
'''
	with conn:
		found = find_task_by_name(conn, task_name)
		if found:
			print('Задача с таким названием уже существует')
		cursor = conn.execute(SQL_INSERT_TASK, (task_name, task_descr, time_plan))


def find_all(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL)
		return cursor.fetchall()


def find_task_by_id(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_ID, (field,))
		return cursor.fetchone()



def find_task_by_time_created(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_TIME_CREATED, (field,))
		return cursor.fetchone()


def find_task_by_name(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_NAME, (field,))
		return cursor.fetchone()


def find_task_by_time_plan(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_TIME_PLAN, (field,))
		return cursor.fetchall()


def find_task_by_date_created(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_TIME_FACT, (field,))
		return cursor.fetchall()


def find_task_by_status(conn, field):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_STATUS, (field,))
		return cursor.fetchall()


def edit_status_done(conn, field):
	with conn:
		cursor = conn.execute(SQL_FINISH_TASK, (field,))


def edit_status_return(conn, field):
	with conn:
		cursor = conn.execute(SQL_RETURN_TASK, (field,))


def del_task(conn, field):
	with conn:
		cursor = conn.execute(SQL_DELETE_TASK, (field,))


def del_done(conn):
	with conn:
		cursor = conn.execute(SQL_DELETE_DONE)


def edit_descr(conn, id):
	with conn:
		cursor = conn.execute(SQL_UPDATE_TASK_DESCR, (id,))


def edit_time_plan(conn, new_time, field):
	with conn:
		cursor = conn.execute(SQL_UPDATE_TASK_PLAN_TIME, (new_time, field))
		return cursor.fetchone()

# python main.py