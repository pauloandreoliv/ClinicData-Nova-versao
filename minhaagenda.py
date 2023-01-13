from config import *

class Ui_ClinicData(object):
    def setupUi(self, ClinicData):

        #Propriedades
        ClinicData.setObjectName("ClinicData")
        ClinicData.resize(1120, 680)
        ClinicData.setMaximumSize(QtCore.QSize(1120, 680))
        font = QtGui.QFont()
        ClinicData.setFont(font)
        ClinicData.setStyleSheet("background-color: white;")
        ClinicData.setWindowTitle("ClinicData")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")

        #Barra azul
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1131, 65))
        self.widget.setStyleSheet("background: #2887BF;")
        self.widget.setObjectName("widget")

        #Label - Minha agenda
        self.texto_boasvindas = QtWidgets.QLabel(self.widget)
        self.texto_boasvindas.setGeometry(QtCore.QRect(20, 8, 731, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.texto_boasvindas.setFont(font)
        self.texto_boasvindas.setStyleSheet("color: white;")
        self.texto_boasvindas.setObjectName("texto_boasvindas")
        self.texto_boasvindas.setText("Minha agenda")

        #Logo
        self.logo_menu = QtWidgets.QLabel(self.widget)
        self.logo_menu.setGeometry(QtCore.QRect(929, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.logo_menu.setFont(font)
        self.logo_menu.setStyleSheet("color: white;")
        self.logo_menu.setText("")
        self.logo_menu.setPixmap(QtGui.QPixmap("midia/logo_menu.png"))
        self.logo_menu.setObjectName("logo_menu")

        try:
            manipulador.execute('SELECT * FROM log_db')
            entrada = list(manipulador.fetchone())
            conexao.commit()
            
            #Função que mostra a tabela
            def funcao_tabela():
                manipulador.execute(f'SELECT nome FROM log_db ORDER BY id')
                lista_logado = list(manipulador.fetchone())
                profissional = str(lista_logado[0]).upper()
                data = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
                manipulador.execute(f'SELECT paciente, data, horario FROM consultas_db WHERE profissional_r = "{profissional}" AND data = "{data}"')
                lista_ = list(manipulador.fetchall())
                print(profissional)
                print(lista_)
                print(data)
                self.tableWidget.insertRow
                self.tableWidget.setColumnCount(3)
                linhas = len(lista_)
                self.tableWidget.setRowCount(linhas)
                cont = 0
                while cont < linhas:
                    cont2 = 0
                    while cont2 < 3:
                        self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista_[cont][cont2])))
                        #Linha, coluna, Item
                        cont2 += 1
                    cont += 1
                    
            #Calendário
            self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
            self.calendarWidget.setGeometry(QtCore.QRect(20, 90, 1051, 421))
            self.calendarWidget.setStyleSheet("color: black;")
            self.calendarWidget.setSelectedDate(QtCore.QDate(2023, 1, 1))
            self.calendarWidget.setMinimumDate(QtCore.QDate(2023, 1, 1))
            self.calendarWidget.setGridVisible(True)
            self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            self.calendarWidget.setObjectName("calendarWidget")

            #Chama função para mostrar a tabela de acordo com a data
            self.calendarWidget.clicked.connect(lambda: funcao_tabela())

            #Tabela
            self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
            self.tableWidget.setGeometry(QtCore.QRect(20, 540, 1051, 131))
            self.tableWidget.setStyleSheet("border: 1px solid silver;")
            self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setRowCount(0)

            #Colunas da tabela
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            self.tableWidget.horizontalHeader().setDefaultSectionSize(345)

            #Inserindo nomes nas colunas da tabela
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("PACIENTE")
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("DATA")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("HORÁRIO")
            
            
        except:
            #Label - Algo deu errado [...]
            self.label_2 = QtWidgets.QLabel(ClinicData)
            self.label_2.setGeometry(QtCore.QRect(0, 510, 1121, 31))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(14)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color: #2887BF;")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.setObjectName("label_2")
            self.label_2.setText("Algo deu errado ao tentar se conectar. Verifique seu login e tente novamente.")

            #Label - Erro de conexão
            self.label = QtWidgets.QLabel(ClinicData)
            self.label.setGeometry(QtCore.QRect(0, 480, 1121, 20))
            font = QtGui.QFont()
            font.setPointSize(17)
            self.label.setFont(font)
            self.label.setStyleSheet("color: #2887BF;")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setText("Erro de conexão")

            #Imagem do erro
            self.img_erro = QtWidgets.QLabel(ClinicData)
            self.img_erro.setGeometry(QtCore.QRect(409, 150, 300, 300))
            self.img_erro.setText("")
            self.img_erro.setPixmap(QtGui.QPixmap("./midia/img_erro.png"))
            self.img_erro.setAlignment(QtCore.Qt.AlignCenter)
            self.img_erro.setObjectName("img_erro")

        #Final - Padrão PyQt
        ClinicData.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    ui = Ui_ClinicData()
    ui.setupUi(ClinicData)
    ClinicData.show()
    sys.exit(app.exec_())
