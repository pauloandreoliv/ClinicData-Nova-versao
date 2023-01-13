import sqlite3
from sqlite3 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
conexao = sqlite3.connect('bd/database.db')
manipulador = conexao.cursor()
class importar:
    def funcao_import():
        import sqlite3
        from sqlite3 import Error
        from PyQt5 import QtCore, QtGui, QtWidgets
        from time import sleep
    funcao_import()
importar()
