from config import *

class Ui_ClinicData_Principal(object):
    def setupUi(self, ClinicData_Principal):

        #Propriedades
        ClinicData_Principal.setObjectName("ClinicData_Principal")
        ClinicData_Principal.resize(1120, 680)
        ClinicData_Principal.setMaximumSize(QtCore.QSize(1120, 680))
        font = QtGui.QFont()
        ClinicData_Principal.setFont(font)
        ClinicData_Principal.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(ClinicData_Principal)
        self.centralwidget.setObjectName("centralwidget")
        ClinicData_Principal.setWindowTitle("ClinicData")

        #Barra azul
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1131, 65))
        self.widget.setStyleSheet("background: #2887BF;")
        self.widget.setObjectName("widget")

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
            #Label - Boas vindas
            self.texto_boasvindas = QtWidgets.QLabel(self.widget)
            self.texto_boasvindas.setGeometry(QtCore.QRect(20, 8, 731, 51))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.texto_boasvindas.setFont(font)
            self.texto_boasvindas.setStyleSheet("color: white;")
            self.texto_boasvindas.setObjectName("texto_boasvindas")

            #Para inserir o nome do(a) administrador(a)/profissional
            manipulador.execute('SELECT nome FROM log_db')
            lista = list(manipulador.fetchone())
            nome_adm = str(lista[0])
            self.texto_boasvindas.setText(f"Olá, {nome_adm}! Seja bem-vindo(a)")
            
            #Menu
            self.widget_2 = QtWidgets.QWidget(self.centralwidget)
            self.widget_2.setGeometry(QtCore.QRect(0, 90, 221, 551))
            self.widget_2.setStyleSheet("")
            self.widget_2.setObjectName("widget_2")

            #Selecionar função
            manipulador.execute('SELECT funcao FROM log_db')
            lista_ = list(manipulador.fetchone())
            if lista_[0] == "PROFISSIONAL":
                
                #Função para mostrar a tabela
                def funcao_tabela(): 
                    manipulador.execute('SELECT nome FROM log_db')
                    lista_ = list(manipulador.fetchone())
                    nome = lista_[0]
                    from datetime import date
                    data = date.today()
                    manipulador.execute(f'SELECT paciente, responsavel, horario, celular, email FROM consultas_db WHERE profissional_r = "{nome}" AND data = "{data}"')
                    lista_ = list(manipulador.fetchall())
                    self.tableWidget.insertRow
                    self.tableWidget.setColumnCount(5)
                    linhas = len(lista_)
                    self.tableWidget.setRowCount(linhas)
                    cont = 0
                    while cont < linhas:
                        cont2 = 0
                        while cont2 < 5:
                            self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista_[cont][cont2])))
                            #Linha, coluna, Item
                            cont2 += 1
                        cont += 1

                #Label - Hoje
                self.texto_info_8 = QtWidgets.QLabel(self.centralwidget)
                self.texto_info_8.setGeometry(QtCore.QRect(270, 190, 41, 41))
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                self.texto_info_8.setFont(font)
                self.texto_info_8.setStyleSheet("color: #5D6C79; background: transparent;")
                self.texto_info_8.setObjectName("texto_info_8")
                self.texto_info_8.setText("Hoje")
                
                #Label - Amanhã você possui X consultas
                self.texto_info_9 = QtWidgets.QLabel(self.centralwidget)
                self.texto_info_9.setGeometry(QtCore.QRect(270, 550, 821, 41))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Light")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(True)
                self.texto_info_9.setFont(font)
                self.texto_info_9.setStyleSheet("color: #5D6C79; background: transparent;")
                self.texto_info_9.setObjectName("texto_info_9")
                self.texto_info_9.setText("Amanhã você possui X consultas. Clique em \"Minha agenda\" para visualizá-las.")

                #Tabela
                self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
                self.tableWidget.setGeometry(QtCore.QRect(270, 230, 821, 321))
                self.tableWidget.setStyleSheet("border: 1px solid silver;")
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setRowCount(0)

                #Colunas da tabela
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(4, item)

                #Títulos das colunas da tabela
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText("PACIENTE")
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText("CELULAR")
                item = self.tableWidget.horizontalHeaderItem(2)
                item.setText("HORÁRIO")
                item = self.tableWidget.horizontalHeaderItem(3)
                item.setText("RESPONSÁVEL")
                item = self.tableWidget.horizontalHeaderItem(4)
                item.setText("E-MAIL")

                #Chama a função que mostra a tabela
                funcao_tabela()
            
            #Função para sair
            def funcao_sair():
                manipulador.execute('DELETE FROM log_db')
                conexao.commit()
                from time import sleep
                sleep(1)
                from login import Ui_ClinicData_Login
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData_Login()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                ClinicData_Principal.close()
                            
            #Botão sair
            self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_10.setGeometry(QtCore.QRect(0, 380, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_10.setFont(font)
            self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_10.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: rgb(255, 48, 48);\n"
    "}")
            self.pushButton_10.setObjectName("pushButton_10")
            self.pushButton_10.setText("Sair")
            self.pushButton_10.clicked.connect(lambda: funcao_sair())

            #Função - Item 1
            def item1():
                from registro import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Anexar registro
            self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_7.setGeometry(QtCore.QRect(0, 245, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_7.setFont(font)
            self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_7.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_7.setObjectName("pushButton_7")
            self.pushButton_7.setText("Anexar registro")
            self.pushButton_7.clicked.connect(lambda:item1())

            #Função - Item 2
            def item2():
                from agendar import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Agendar consulta
            self.pushButton = QtWidgets.QPushButton(self.widget_2)
            self.pushButton.setGeometry(QtCore.QRect(0, 20, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton.setFont(font)
            self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setText("Agendar consulta")
            self.pushButton.clicked.connect(lambda:item2())

            #Função - Item 3
            def item3():
                from consultas import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Consultas existentes
            self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_2.setGeometry(QtCore.QRect(0, 65, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_2.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_2.setText("Consultas existentes")
            self.pushButton_2.clicked.connect(lambda:item3())

            #Função - Item 4
            def item4():
                from minhaagenda import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Minha agenda
            self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_8.setGeometry(QtCore.QRect(0, 290, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_8.setFont(font)
            self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_8.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_8.setObjectName("pushButton_8")
            self.pushButton_8.setText("Minha agenda")
            self.pushButton_8.clicked.connect(lambda:item4())

            #Função - Item 5
            def item5():
                from profissionais import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Profissionais
            self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_9.setGeometry(QtCore.QRect(0, 335, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_9.setFont(font)
            self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_9.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_9.setObjectName("pushButton_9")
            self.pushButton_9.setText("Profissionais")
            self.pushButton_9.clicked.connect(lambda:item5())

            #Função - Item 6
            def item6():
                from historico import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Histórico de consultas
            self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_5.setGeometry(QtCore.QRect(0, 200, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_5.setFont(font)
            self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_5.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_5.setText("Histórico de consultas")
            self.pushButton_5.clicked.connect(lambda:item6())

            #Função - Item 7
            def item7():
                from cadastrar import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Cadastrar paciente
            self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_3.setGeometry(QtCore.QRect(0, 110, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_3.setFont(font)
            self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_3.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_3.setText("Cadastrar paciente")
            self.pushButton_3.clicked.connect(lambda:item7())

            #Função - Item 8
            def item8():
                from pacientes import Ui_ClinicData
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_ClinicData()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                
            #Botão Pacientes cadastrados
            self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
            self.pushButton_4.setGeometry(QtCore.QRect(0, 155, 251, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            font.setPointSize(12)
            self.pushButton_4.setFont(font)
            self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_4.setStyleSheet("QPushButton{\n"
    "color: #5D6C79;\n"
    "text-align: left;\n"
    "padding-left: 22px;\n"
    "border: none;\n"
    "}\n"
    "QPushButton:hover{\n"
    "color: #2887BF;\n"
    "}")
            self.pushButton_4.setObjectName("pushButton_4")
            self.pushButton_4.setText("Pacientes cadastrados")
            self.pushButton_4.clicked.connect(lambda:item8())

            #Caixa - Pacientes
            self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox.setGeometry(QtCore.QRect(270, 100, 261, 91))
            self.groupBox.setStyleSheet("background: #2887BF; border-radius: 10px; border: none;")
            self.groupBox.setTitle("")
            self.groupBox.setObjectName("groupBox")
            #*ícone
            self.label = QtWidgets.QLabel(self.groupBox)
            self.label.setGeometry(QtCore.QRect(30, 28, 61, 71))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("midia/pacientes.png"))
            self.label.setObjectName("label")
            #*número
            self.texto_info_2 = QtWidgets.QLabel(self.groupBox)
            self.texto_info_2.setGeometry(QtCore.QRect(90, 10, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setBold(True)
            self.texto_info_2.setFont(font)
            self.texto_info_2.setStyleSheet("color: white;")
            self.texto_info_2.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_2.setObjectName("texto_info_2")
            manipulador.execute('SELECT COUNT(paciente) FROM pacientes_db')
            num = list(manipulador.fetchone())
            num = num[0]
            self.texto_info_2.setText(f"{num}")
            #*pacientes
            self.texto_info_3 = QtWidgets.QLabel(self.groupBox)
            self.texto_info_3.setGeometry(QtCore.QRect(90, 30, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            self.texto_info_3.setFont(font)
            self.texto_info_3.setStyleSheet("color: white; background: transparent;")
            self.texto_info_3.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_3.setObjectName("texto_info_3")
            self.texto_info_3.setText("pacientes")

            #Caixa - Consultas
            self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox_2.setGeometry(QtCore.QRect(550, 100, 261, 91))
            self.groupBox_2.setStyleSheet("background: #2887BF; border-radius: 10px; border: none;")
            self.groupBox_2.setTitle("")
            self.groupBox_2.setObjectName("groupBox_2")
            #*ícone
            self.label_2 = QtWidgets.QLabel(self.groupBox_2)
            self.label_2.setGeometry(QtCore.QRect(30, 10, 71, 71))
            self.label_2.setText("")
            self.label_2.setPixmap(QtGui.QPixmap("midia/consultas.png"))
            self.label_2.setObjectName("label_2")
            #*número
            self.texto_info_4 = QtWidgets.QLabel(self.groupBox_2)
            self.texto_info_4.setGeometry(QtCore.QRect(90, 10, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setBold(True)
            self.texto_info_4.setFont(font)
            self.texto_info_4.setStyleSheet("color: white;")
            self.texto_info_4.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_4.setObjectName("texto_info_4")
            manipulador.execute('SELECT COUNT(paciente) FROM consultas_db')
            num = list(manipulador.fetchone())
            num = num[0]
            self.texto_info_4.setText(f"{num}")
            #*consultas
            self.texto_info_5 = QtWidgets.QLabel(self.groupBox_2)
            self.texto_info_5.setGeometry(QtCore.QRect(90, 30, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            self.texto_info_5.setFont(font)
            self.texto_info_5.setStyleSheet("color: white; background: transparent;")
            self.texto_info_5.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_5.setObjectName("texto_info_5")
            self.texto_info_5.setText("consultas")

            #Caixa - Profissionais
            self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox_3.setGeometry(QtCore.QRect(830, 100, 261, 91))
            self.groupBox_3.setStyleSheet("background: #2887BF; border-radius: 10px; border: none;")
            self.groupBox_3.setTitle("")
            self.groupBox_3.setObjectName("groupBox_3")
            #*ícone
            self.label_3 = QtWidgets.QLabel(self.groupBox_3)
            self.label_3.setGeometry(QtCore.QRect(30, 20, 61, 71))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap("midia/profissionais.png"))
            self.label_3.setObjectName("label_3")
            #*número
            self.texto_info_6 = QtWidgets.QLabel(self.groupBox_3)
            self.texto_info_6.setGeometry(QtCore.QRect(90, 10, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(13)
            font.setBold(True)
            self.texto_info_6.setFont(font)
            self.texto_info_6.setStyleSheet("color: white;")
            self.texto_info_6.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_6.setObjectName("texto_info_6")
            manipulador.execute('SELECT COUNT(nome) FROM profissionais')
            num = list(manipulador.fetchone())
            num = num[0]
            self.texto_info_6.setText(f"{num}")
            #*profissionais
            self.texto_info_7 = QtWidgets.QLabel(self.groupBox_3)
            self.texto_info_7.setGeometry(QtCore.QRect(90, 30, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            self.texto_info_7.setFont(font)
            self.texto_info_7.setStyleSheet("color: white; background: transparent;")
            self.texto_info_7.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_info_7.setObjectName("texto_info_7")
            self.texto_info_7.setText("profissionais")
                
            self.texto_boasvindas.raise_()
            
        except:
            #Label - Algo deu errado [...]
            self.label_2 = QtWidgets.QLabel(ClinicData_Principal)
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
            self.label = QtWidgets.QLabel(ClinicData_Principal)
            self.label.setGeometry(QtCore.QRect(0, 480, 1121, 20))
            font = QtGui.QFont()
            font.setPointSize(17)
            self.label.setFont(font)
            self.label.setStyleSheet("color: #2887BF;")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setText("Erro de conexão")

            #Imagem do erro
            self.img_erro = QtWidgets.QLabel(ClinicData_Principal)
            self.img_erro.setGeometry(QtCore.QRect(409, 150, 300, 300))
            self.img_erro.setText("")
            self.img_erro.setPixmap(QtGui.QPixmap("./midia/img_erro.png"))
            self.img_erro.setAlignment(QtCore.Qt.AlignCenter)
            self.img_erro.setObjectName("img_erro")

        #Final - Padrão PyQt
        ClinicData_Principal.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ClinicData_Principal)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData_Principal = QtWidgets.QMainWindow()
    ui = Ui_ClinicData_Principal()
    ui.setupUi(ClinicData_Principal)
    ClinicData_Principal.show()
    sys.exit(app.exec_())
