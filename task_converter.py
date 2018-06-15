import sys
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
	QApplication, QMainWindow, QWidget, 
	QLabel, QDoubleSpinBox, QPushButton, 
	QVBoxLayout
)

from urllib.request import urlopen
from lxml import etree
#QDoubleSpinBox - для ввода дробных чисел, QSpinBox - целых чисел

class Course(QObject):
	CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

	def get(self):
		with urlopen(self.CBR_URL) as r:
			tree = etree.parse(r)      # открытый объект ввода-вывода
			value = tree.xpath('*[@ID="R01235"]/Value')[0].text  #0й элемент, получи текстовый элемент
			return float(value.replace(',', '.'))

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._initUi()
		self._initSignals()
		self._initLayouts()


	def _initUi(self):
		self.setWindowTitle('Конвертер валют')

		self.srcLabel = QLabel('Сумма в рублях', self) # исходный
		self.resultLabel = QLabel('Сумма в долларах', self)

		self.srcAmountEdit = QDoubleSpinBox(self)
		# http://doc.qt.io/qt-5/qdoublespinbox.html
		# ~ - деструктор
		self.srcAmountEdit.setMaximum(99999999)  # Меняем ограничение на макс значение
		self.resultAmountEdit = QDoubleSpinBox(self)
		self.resultAmountEdit.setMaximum(999999999)

		self.convertBtn = QPushButton('Перевести', self)
		#self.convertBtn.setDefault(True)
		self.cleanBtn = QPushButton('Очистить', self)
		#self.ReturnPress = keyPressEvent(self)


	def _initSignals(self):
		self.convertBtn.clicked.connect(self.onClickConvertBtn) # ссылаемся на метод, а не вызываем
		self.cleanBtn.clicked.connect(self.onClickCleanBtn)

	def keyPressEvent(self,e):
		if e.key() == Qt.Key_Return:
			self.onClickConvertBtn()


	def _initLayouts(self):
		w = QWidget(self)               # промежуточный виджет для слоя
		self.mainLayout = QVBoxLayout(w) # нужен промежуточный виджет, к которому применим слой

		self.mainLayout.addWidget(self.srcLabel)  # новый виджет добавляется в конец
		self.mainLayout.addWidget(self.srcAmountEdit)
		self.mainLayout.addWidget(self.resultLabel)
		self.mainLayout.addWidget(self.resultAmountEdit)
		self.mainLayout.addWidget(self.convertBtn)
		self.mainLayout.addWidget(self.cleanBtn)

		self.setCentralWidget(w)

	def onClickConvertBtn(self):
		value = self.srcAmountEdit.value()
		value2 = self.resultAmountEdit.value()
		# те виджеты, которые ждут ввода чисел, имеют метод value и setValue
		# текст - Text, setText
		# и то, и другое (напр, выбор из списка)
		if value and not value2:
			self.resultAmountEdit.setValue(value / Course().get())
			self.convertBtn.setEnabled(False)
		if value2 and not value:
			self.srcAmountEdit.setValue(value2 * Course().get())
			self.convertBtn.setEnabled(False)
		#else:
		#	self.convertBtn.setEnabled(False)
	'''
	def check(self):
		if value and not value2 or not value and value2:
			self.convertBtn.setEnabled(True)
		else:
			self.convertBtn.setEnabled(False)
	'''	
	def onClickCleanBtn(self):
		self.resultAmountEdit.setValue(0)
		self.srcAmountEdit.setValue(0)
		self.convertBtn.setEnabled(True)

if __name__ == "__main__":
	app = QApplication(sys.argv)  # аргументы командной строки в виде списка - из sys

	converter = MainWindow() 
	converter.show()

	sys.exit(app.exec_())
	def onClickConvertBtn(self):
		pass

'''
слои занимаются группировкой:
QHBoxLayout - горизонтальное расположение неск окон в одном
QVBoxLayout - вертикальное (столбцом)
QFormLayout - таблица (1й ст - Qlabel, 2й ст - QWidgets)
QGridLayout -  таблица с возможостью объединения соседних (в любую сторону) ячеек

в слои не передаем родителя (self)

здесь под "parent" подразумевается тот виджет, к которому хотим применить
'''

''' MainWindow
сверху - QMenuBar (необяз)
	состоит из QMenu (каждая выпадающая вкладка)
		состоит из QAction

QToolBar - Иконки инструментов (save, ...)   (необяз)

QDocWidget

QStatusBar - строка состояния (можно выводить сообщения)


CentralWidget - всегда есть и можем менять

'''
# Enter - keyReturn