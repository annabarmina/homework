from pony.orm import Database, Required, Optional, Set, PrimaryKey, db_session
from datetime import datetime


db = Database()


class MyEntity(db.Entity):
	attr1 = Required(str)


class Product(db.Entity):
	title = Required(str)
	price = Required(float)
	description = Optional(str)  # По умолчанию - пустая строка
	unit = Required(str)
	category = Required('Category') # pony требует обратную ссылку (двусторонняя связь!!!)
	# alt_categories = list('Category')
	# alt_categories = Set('Category') - пришлось бы в категории прописать, на какое именно совйство Product ссылка
	# amount = int # наличие товара
	# PrimaryKey создается автоматически - id
	history = Set('ProductHistory') # обратное св-во
	orderitems = Set('OrderItem')
	cartitem = Set('CartItem')

class ProductHistory(db.Entity):
	product = Required('Product')
	created = Optional(datetime, default=datetime.now)
	price = Required(float)


class Category(db.Entity):
	""" Категория товаров """
	parent = Optional('Category', reverse = 'parent')
	title = Required(str)
	products = Set('Product') # обратная ссылка к Product

class Customer(db.Entity):
	""" Покупатель """
	email = Required(str)
	phone = Optional(str)
	name = Optional(str)
	addresses = Set('Address')
	orders = Set('Order')
	carts = Set('Cart')

class Address(db.Entity):
	""" Адрес """
	customer = Required('Customer')
	country = Required(str)
	city = Required(str)
	street = Required(str)
	zipcode = Required(str)
	house = Required(int)
	flat = Required(int)
		
class Cart(db.Entity):
	""" Корзина с товарами """
	customer = Required('Customer')
	products = Set('CartItem')

class CartItem(db.Entity):
	cart = Required('Cart')
	product = Required('Product')
	amount = Required(int)	

class Order(db.Entity):
	""" Заказ """
	customer = Required('Customer')
	created = Optional(datetime, default=datetime.now)
	products = Set('OrderItem')
	status = Required('Status')

class OrderItem(db.Entity):
	""" Товар (одна позиция) в заказе """
	order = Required('Order')	
	product = Required('Product')
	amount = Required(int)  # 1 единица товара

class Status(db.Entity):
	""" Статус """
	name = Required(str)
	statuses = Set('Order')

class Menu(db.Entity):
	pass


db.bind(provider='sqlite', filename='shop.sqlite', create_db=True)

db.generate_mapping(create_tables=True)
#sql_debug(True)

@db_session
def add_category():
	с1 = Category(title = 'Drinks')
	c2 = Category(title = 'Food')

@db_session
def add_product():
	
	p1 = Product(title = 'Beer', price = '70', unit = 'шт', category=Category[1])
	#с1 = Category(title = 'Drinks', products = (p1))

@db_session
def add_customer():
	cust1 = Customer(email = 'pokupatel@gmail.com')

add_category()
add_product()
add_customer()

"""
ORM
object related mapping

Poni:
- быстрый (для вэба)
- проще синтаксис (чем в Алхимии)

поиск в google про framework (только офиц сайты!):
"ponyorm" -> docs : https://docs.ponyorm.com/

виртуальное укружение (модуль venv - vertal enviroment)
-m - это возможность подгрузить модуль

python -m venv env
(pip install venv)

<venv>\Scripts\activate.bat
D:\Python\shop\env\Scripts\activate.bat
pip install pony

Д/З.1. что такое вирт.окружение, и убедиться, что оно работает

в пони для описания сущности нужно создать DataBase:
from pony.orm import Database

db = Database()

все сущности наследуем от entity

from pony.orm import Database, Required (обяз.свойства),
 Optional (доп), Set (множество, напр.ссылка на коллекцию), PrimaryKey
"""