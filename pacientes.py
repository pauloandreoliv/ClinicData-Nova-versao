from config import *

class Ui_ClinicData(object):
    def setupUi(self, ClinicData):

        #Propriedades
        ClinicData.setObjectName("ClinicData")
        ClinicData.resize(1120, 680)
        ClinicData.setMaximumSize(QtCore.QSize(1120, 680))
        ClinicData.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")
        ClinicData.setWindowTitle("ClinicData")

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
            manipulador.execute('SELECT * FROM log_db')
            entrada = list(manipulador.fetchone())
            conexao.commit()

            #Label - Boas vindas
            self.texto_boasvindas = QtWidgets.QLabel(self.widget)
            self.texto_boasvindas.setGeometry(QtCore.QRect(20, 8, 731, 51))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.texto_boasvindas.setFont(font)
            self.texto_boasvindas.setStyleSheet("color: white;")
            self.texto_boasvindas.setObjectName("texto_boasvindas")
            self.texto_boasvindas.setText("Visualizar pacientes")
        
            #Label - Erro 2
            self.texto_erro_2 = QtWidgets.QLabel(self.centralwidget)
            self.texto_erro_2.setGeometry(QtCore.QRect(20, 150, 471, 16))
            self.texto_erro_2.setStyleSheet("color: #ED8686;")
            self.texto_erro_2.setObjectName("texto_erro_2")

            #Label - Configurando
            self.texto_configurando = QtWidgets.QLabel(self.centralwidget)
            self.texto_configurando.setGeometry(QtCore.QRect(20, 180, 831, 16))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(False)
            self.texto_configurando.setFont(font)
            self.texto_configurando.setStyleSheet("color: #2887BF;")
            self.texto_configurando.setObjectName("texto_configurando")
            self.texto_configurando.setText("")

            #Label - Pesquisar
            self.texto_pesquisar = QtWidgets.QLabel(self.centralwidget)
            self.texto_pesquisar.setGeometry(QtCore.QRect(50, 80, 131, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_pesquisar.setFont(font)
            self.texto_pesquisar.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_pesquisar.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_pesquisar.setObjectName("texto_pesquisar")
            self.texto_pesquisar.setText("Pesquisar paciente")

            #Input - Pesquisar
            self.pesquisar = QtWidgets.QLineEdit(self.centralwidget)
            self.pesquisar.setGeometry(QtCore.QRect(20, 90, 1009, 51))
            font = QtGui.QFont()
            self.pesquisar.setFont(font)
            self.pesquisar.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6;padding: 5px;")
            self.pesquisar.setText("")
            self.pesquisar.setAlignment(QtCore.Qt.AlignLeft)
            self.pesquisar.setClearButtonEnabled(False)
            self.pesquisar.setObjectName("pesquisar")
            
            #Tabela
            self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
            self.tableWidget.setGeometry(QtCore.QRect(20, 210, 1051, 401))
            self.tableWidget.setStyleSheet("border: 1px solid silver;")
            self.tableWidget.setObjectName("tableWidget")

            #Função nada
            def funcao_nada():
                return

            #Função que mostra a tabela
            def funcao_tabela():
                manipulador.execute('SELECT * FROM pacientes_db ORDER BY id')
                lista_ = list(manipulador.fetchall())
                self.tableWidget.insertRow
                self.tableWidget.setColumnCount(14)
                linhas = len(lista_)
                self.tableWidget.setRowCount(linhas)
                cont = 0
                while cont < linhas:
                    cont2 = 0
                    while cont2 < 14:
                        self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista_[cont][cont2])))
                        #Linha, coluna, Item
                        cont2 += 1
                    cont += 1
                    
            funcao_tabela()

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
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(5, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(6, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(7, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(8, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(9, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(10, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(11, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(12, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(13, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(14, item)

            #Inserindo títulos das colunas
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("FREQUÊNCIA")
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("PACIENTE")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("CÓDIGO")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("RESPONSÁVEL")
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText("OBSERVAÇÕES")
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText("E-MAIL")
            item = self.tableWidget.horizontalHeaderItem(6)
            item.setText("CELULAR")
            item = self.tableWidget.horizontalHeaderItem(7)
            item.setText("LAUDO")
            item = self.tableWidget.horizontalHeaderItem(8)
            item.setText("ENDEREÇO")
            item = self.tableWidget.horizontalHeaderItem(9)
            item.setText("PROFISSIONAL")
            item = self.tableWidget.horizontalHeaderItem(10)
            item.setText("ESCOLA")
            item = self.tableWidget.horizontalHeaderItem(11)
            item.setText("NASCIMENTO")
            item = self.tableWidget.horizontalHeaderItem(12)
            item.setText("CPF")
            item = self.tableWidget.horizontalHeaderItem(13)
            item.setText("ID")

            #Função que pega o nome do paciente e coloca na variável nome
            def funcao_pega_nome():
                linha_ = self.tableWidget.currentItem().row()
                nome = str(self.tableWidget.item(linha_,1).text())
                self.texto_configurando.setText(f"Você está configurando {nome}")
            
            #Botão que chama a função pega_nome
            self.tableWidget.itemClicked.connect(lambda: funcao_pega_nome())

            #Janela de aviso de download da planilha
            def funcao_aviso(parametro):
                from PyQt5.QtWidgets import QMessageBox
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Aviso")
                if parametro == "downloadsucesso":
                    msg.setText("O seu download foi concluído com sucesso.")
                if parametro == "downloaderro":
                    msg.setText("Houve um erro ao tentar realizar o seu download.")
                if parametro == "edicao":
                    msg.setText("Editado com sucesso.")
                if parametro == "exclusao":
                    msg.setText("Apagado com sucesso.")
                if parametro == "erro":
                    msg.setText("Erro ao tentar executar ação. Tente novamente.")
                executar = msg.exec()
            
            #Função de edição
            def funcao_editar():
                if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                    linha_tb = self.tableWidget.currentItem()
                    if linha_tb != None:
                        linha_tb = self.tableWidget.currentItem().row()
                        linha_tb = int(linha_tb)
                        freq_ = self.tableWidget.item(linha_tb,0).text().upper()
                        paciente_ = self.tableWidget.item(linha_tb,1).text().upper()
                        responsavel_ = self.tableWidget.item(linha_tb,3).text().upper()
                        observacoes_ = self.tableWidget.item(linha_tb,4).text().upper()
                        email_ = self.tableWidget.item(linha_tb,5).text().upper()
                        celular_ = self.tableWidget.item(linha_tb,6).text()
                        laudo_ = self.tableWidget.item(linha_tb,7).text()
                        endereco_ = self.tableWidget.item(linha_tb,8).text()
                        profissional_ = self.tableWidget.item(linha_tb,9).text()
                        escola_ = self.tableWidget.item(linha_tb,10).text()
                        nascimento_ = str(self.tableWidget.item(linha_tb,11).text())
                        cpf_ = self.tableWidget.item(linha_tb,12).text()
                        id_ = int(self.tableWidget.item(linha_tb,13).text())
                        import sqlite3
                        from sqlite3 import Error
                        from config import conexao, manipulador
                        manipulador.execute(f"UPDATE pacientes_db SET frequencia = '{freq_}', paciente = '{paciente_}', responsavel = '{responsavel_}', profissional = '{profissional_}', escola = '{escola_}', cpf = '{cpf_}', celular = '{celular_}', nascimento = '{nascimento_}', email = '{email_}', laudo = '{laudo_}', endereco = '{endereco_}', observacoes = '{observacoes_}' WHERE id = {id_}")
                        conexao.commit()
                        funcao_aviso("edicao")
                else:
                    funcao_aviso("erro")
                    
            #Botão editar
            self.botao_editar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_editar.setGeometry(QtCore.QRect(920, 630, 75, 24))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_editar.setFont(font)
            self.botao_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_editar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_editar.setObjectName("botao_editar")
            self.botao_editar.setText("Editar")
            self.botao_editar.clicked.connect(lambda: funcao_editar())

            #Função de exclusão de um item específico
            def funcao_excluir():
                if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                    linha_tb = self.tableWidget.currentItem()
                    if linha_tb != None:
                        linha_tb = self.tableWidget.currentItem().row()
                        linha_tb = int(linha_tb)
                        id_ = int(self.tableWidget.item(linha_tb,13).text())
                        import sqlite3
                        from sqlite3 import Error
                        from config import conexao, manipulador
                        manipulador.execute(f"DELETE FROM pacientes_db WHERE id = {id_}")
                        conexao.commit()
                        funcao_aviso("exclusao")
                else:
                    funcao_aviso("erro")
                        
            #Botão excluir
            self.botao_excluir = QtWidgets.QPushButton(self.centralwidget)
            self.botao_excluir.setGeometry(QtCore.QRect(1010, 630, 75, 24))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_excluir.setFont(font)
            self.botao_excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_excluir.setStyleSheet("border: none; color: #2887BF;")
            self.botao_excluir.setObjectName("botao_excluir")
            self.botao_excluir.setText("Excluir")
            self.botao_excluir.clicked.connect(lambda: funcao_excluir())

            #Função para baixar planilha
            def funcao_baixar():
                    try:
                            from openpyxl import Workbook
                            if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                                planilha = Workbook()
                                planilha.create_sheet(index = 0, title = "Pacientes")
                                folha = planilha["Pacientes"]
                                folha.append(['PAGO','PACIENTE','CÓDIGO','RESPONSÁVEL','PROFISSIONAL','HORÁRIO','DATA','CELULAR','VALOR','E-MAIL','LAUDO','ENDEREÇO','OBSERVAÇÕES','ID'])

                                cont = 0
                                while cont < int(self.tableWidget.rowCount()):
                                        cont2 = 0
                                        linha = []
                                        while cont2 < int(self.tableWidget.columnCount()):
                                            linha.append(self.tableWidget.item(cont, cont2).text())
                                            #Linha, coluna, Item
                                            cont2 += 1
                                        folha.append(linha)#Adiciona a linha na tabela
                                        cont += 1

                                from os import path, mkdir, listdir
                                import platform
                                if str(platform.system()) == str("Windows"): #Para salvar caso seja Windows
                                    pasta = path.join(path.expanduser("~\Documents"))
                                    pasta_existe = path.exists(pasta)
                                    if pasta_existe == True:
                                        pasta_clinicdata = path.join(path.expanduser("~\Documents\\Planilhas - ClinicData"))
                                        pasta_clinicdata_existe = path.exists(pasta_clinicdata)#Verifica se a pasta existe
                                    if pasta_clinicdata_existe == False:
                                        mkdir(pasta_clinicdata)#Caso a pasta não exista, cria a pasta
                                        
                                    if listdir(pasta_clinicdata) == [] or "pacientes.xlsx" not in listdir(pasta_clinicdata):
                                        nome = "pacientes.xlsx"
                                    else:
                                        numero = 1
                                        for k in range(0,len(listdir(pasta_clinicdata))):
                                            nome = str("pacientes" + "(" + str(numero) + ")" + ".xlsx")
                                            if nome in listdir(pasta_clinicdata):
                                                numero +=1
                                    planilha.save(pasta_clinicdata + "\\" + nome)#Salva a planilha na pasta
                                else: #Para salvar nos outros sistemas
                                    planilha.save("pacientes.xlsx")#Salva a planilha na pasta
                                funcao_aviso("downloadsucesso")
                            else:
                                funcao_aviso("downloaderro")
                    except:
                        funcao_aviso("downloaderro")
                
                
            #Botão baixar
            self.botao_baixar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_baixar.setGeometry(QtCore.QRect(1034, 170, 41, 31))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_baixar.setFont(font)
            self.botao_baixar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_baixar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_baixar.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("midia/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botao_baixar.setIcon(icon)
            self.botao_baixar.setIconSize(QtCore.QSize(30, 30))
            self.botao_baixar.setObjectName("botao_baixar")
            self.botao_baixar.clicked.connect(lambda: funcao_baixar())

            #Função pesquisar - Seleciona o dado da base de dados que possui o valor (nome completo ou código) pesquisado
            def funcao_pesquisar():
                self.texto_erro_2.setText("")
                pesquisar = self.pesquisar.text().upper().strip()
                self.tableWidget.setRowCount(0)
                
                if pesquisar != '':
                    numeros = []
                    for numero in list(range(0,11)):
                        numeros.append(str(numero))
                        
                    string_codigo = ''
                    for num in pesquisar:
                        if num in numeros:
                            string_codigo += str(num)
                            
                    if string_codigo != '':
                        manipulador.execute(f'SELECT * FROM pacientes_db WHERE codigo LIKE "%{pesquisar}%"')
                        lista = list(manipulador.fetchall())
                        self.tableWidget.setRowCount(len(lista))
                        cont = 0
                        while cont < len(lista):
                            cont2 = 0
                            while cont2 < 14:
                                self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista[cont][cont2])))
                                #Linha, coluna, Item
                                cont2 += 1
                            cont += 1
                            
                    if string_codigo == '':
                        manipulador.execute(f'SELECT * FROM pacientes_db WHERE paciente LIKE "%{pesquisar}%"')
                        lista = list(manipulador.fetchall())
                        self.tableWidget.setRowCount(len(lista))
                        cont = 0
                        while cont < len(lista):
                            cont2 = 0
                            while cont2 < 14:
                                self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista[cont][cont2])))
                                #Linha, coluna, Item
                                cont2 += 1
                            cont += 1
                    
                    if int(self.tableWidget.rowCount()) == 0:
                        self.texto_erro_2.setText("Nome inexistente ou incorreto")
                    else:
                        self.texto_erro_2.setText("")
                else:
                    self.texto_erro_2.setText("")
                    funcao_tabela()
                    
            #Botão pesquisar
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(1033, 90, 41, 51))
            self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton.setStyleSheet("border: none;")
            self.pushButton.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("midia/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon1)
            self.pushButton.setIconSize(QtCore.QSize(25, 25))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(lambda: funcao_pesquisar())

            #Final - Padrão PyQt
            self.texto_boasvindas.raise_()
            self.logo_menu.raise_()
            self.texto_pesquisar.raise_()

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
