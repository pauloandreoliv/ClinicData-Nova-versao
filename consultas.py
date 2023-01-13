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
            self.texto_boasvindas.setText("Visualizar consultas")
        
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
            self.texto_pesquisar.setText("Pesquisar consulta")

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
                manipulador.execute('SELECT * FROM consultas_db WHERE apagado = "n" ORDER BY id')
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

            #Inserindo títulos das colunas
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("PAGO")
            item = self.tableWidget.horizontalHeaderItem(1)
            item.setText("PACIENTE")
            item = self.tableWidget.horizontalHeaderItem(2)
            item.setText("CÓDIGO")
            item = self.tableWidget.horizontalHeaderItem(3)
            item.setText("RESPONSÁVEL")
            item = self.tableWidget.horizontalHeaderItem(4)
            item.setText("PROFISSIONAL")
            item = self.tableWidget.horizontalHeaderItem(5)
            item.setText("HORÁRIO")
            item = self.tableWidget.horizontalHeaderItem(6)
            item.setText("DATA")
            item = self.tableWidget.horizontalHeaderItem(7)
            item.setText("CELULAR")
            item = self.tableWidget.horizontalHeaderItem(8)
            item.setText("VALOR")
            item = self.tableWidget.horizontalHeaderItem(9)
            item.setText("E-MAIL")
            item = self.tableWidget.horizontalHeaderItem(10)
            item.setText("LAUDO")
            item = self.tableWidget.horizontalHeaderItem(11)
            item.setText("ENDEREÇO")
            item = self.tableWidget.horizontalHeaderItem(12)
            item.setText("OBSERVAÇÕES")
            item = self.tableWidget.horizontalHeaderItem(13)
            item.setText("ID")

            #Função que pega o nome do paciente e coloca na variável nome
            def funcao_pega_nome():
                linha_ = self.tableWidget.currentItem().row()
                nome = str(self.tableWidget.item(linha_,1).text())
                self.texto_configurando.setText(f"Você está configurando {nome}")
            
            #Botão que chama a função pega_nome
            self.tableWidget.itemClicked.connect(lambda: funcao_pega_nome())

            #Função de avisos
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
                if parametro == "emailsucesso":
                    msg.setText("E-mail enviado com sucesso.")
                executar = msg.exec()

            
            #Função para enviar e-mail
            def funcao_enviar_email():
                if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                    linha_tb = self.tableWidget.currentItem()
                    if linha_tb != None:
                        linha_tb = self.tableWidget.currentItem().row()
                        linha_tb = int(linha_tb)
                        try:
                            email_do_paciente = str(self.tableWidget.item(linha_tb,9).text()).lower()
                            nome_do_paciente = str(self.tableWidget.item(linha_tb,1).text()).upper()

                            manipulador.execute(f"SELECT * FROM clinica_db")
                            dados_ = list(manipulador.fetchone())
                            nome = dados_[0]
                            endereco = dados_[1]
                            ddd = dados_[2]
                            whatsapp = dados_[3]
                            contato = dados_[4]
                            email_ = dados_[5]
                            senha_ = dados_[6]

                            profissional = str(self.tableWidget.item(linha_tb,4).text())
                            horario = str(self.tableWidget.item(linha_tb,5).text())
                            data = str(self.tableWidget.item(linha_tb,6).text())
                            
                            from email.mime.multipart import MIMEMultipart as formatodoemail
                            from email.mime.text import MIMEText as textodoemail
                            import smtplib

                            conectar = smtplib.SMTP("smtp-mail.outlook.com",587) #Conecta ao servidor
                            conectar.starttls() #Transporte layer security
                            conectar.login(f"{email_}", f"{senha_}") #Realiza o login

                            mensagem = formatodoemail()
                            HTML = f"""
                            <body>
                            <div style="height:200px;">
                            <center>
                            <div style="background-image: url(https://i.imgur.com/9xFUPqn.png); width: 294px; height: 85px;margin-top: 40px;margin-left:-25px;"></div></center>
                            <p style="color: #2887bf;text-align: center;font-size: 14px;padding-top: 25px;font-weight: bold;letter-spacing: 10px;">AVISO</p>
                            </div>
                            <div style="text-align: center;">
                            <h1>Olá, {nome_do_paciente}!</h1>
                            <h2 style="font-size: 20px;">Você está lembrado(a) da sua consulta no dia <div style="display: inline-block;color: #4a66a2;text-decoration: underline;">{data}</div>?</h2>
                            <div style="border: 1px solid silver;padding: 10px;border-radius: 10px;">
                            <div style="border-bottom: 1px solid silver;">

                            <div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Endereço:<div style="display: inline;font-weight: bold;margin-left: 5px;">{endereco}</div></div></div>
                            <div style="border-bottom: 1px solid silver;"><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;"> Horário: <div style="display: inline;font-weight: bold;margin-left: 5px;">{horario}</div></div>

                            </div>
                            <div style=""><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Profissional:<div style="display: inline;font-weight: bold;margin-left: 5px;">{profissional}</div></div>

                            </div>
                            </div>


                            <div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">WhatsApp: ({ddd}) {whatsapp}</div><div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">E-mail: {contato}</div>

                            <p>Em caso de cancelamento, adiamento ou dúvidas entre em contato conosco pelos nossos canais de comunicação o mais rápido possível!</p>
                            <p>Nós agradecemos pela compreensão :)</p>
                            <p>Equipe {nome}</p><p style="font-size: 12px;margin-top: 50px;color: silver;">E-MAIL ENVIADO AUTOMATICAMENTE. POR FAVOR, NÃO RESPONDER</p></div>
                            </body>
                            """
                            mensagem['Subject'] = f"AVISO - {nome}" #Assunto do e-mail
                            mensagem.attach(textodoemail(HTML,'html')) #Conteúdo do texto//Lê em formato HTML
                            texto = mensagem.as_string() #Coloca como string

                            conectar.sendmail(f"{email_}",email_do_paciente,texto) #Envia o e-mail
                            conectar.close()
                            funcao_aviso("emailsucesso")
                        except:
                            funcao_aviso("erro")
                else:
                    funcao_aviso("erro")
                    
            #Botão lembrar
            self.botao_lembrar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_lembrar.setGeometry(QtCore.QRect(20, 630, 41, 31))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_lembrar.setFont(font)
            self.botao_lembrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_lembrar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_lembrar.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("midia/sino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botao_lembrar.setIcon(icon2)
            self.botao_lembrar.setIconSize(QtCore.QSize(30, 30))
            self.botao_lembrar.setObjectName("botao_lembrar")
            self.botao_lembrar.clicked.connect(lambda: funcao_enviar_email())

            #Função para enviar e-mail (cancelamento)
            def funcao_enviar_email_cancelamento():
                if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                    linha_tb = self.tableWidget.currentItem()
                    if linha_tb != None:
                        linha_tb = self.tableWidget.currentItem().row()
                        linha_tb = int(linha_tb)
                        try:
                            email_do_paciente = str(self.tableWidget.item(linha_tb,9).text()).lower()
                            nome_do_paciente = str(self.tableWidget.item(linha_tb,1).text()).upper()

                            manipulador.execute(f"SELECT * FROM clinica_db") #Pega os dados da clínica
                            dados_ = list(manipulador.fetchone())
                            nome = dados_[0]
                            endereco = dados_[1]
                            ddd = dados_[2]
                            whatsapp = dados_[3]
                            contato = dados_[4]
                            email_ = dados_[5]
                            senha_ = dados_[6]

                            profissional = str(self.tableWidget.item(linha_tb,4).text())
                            horario = str(self.tableWidget.item(linha_tb,5).text())
                            data = str(self.tableWidget.item(linha_tb,6).text())
                            
                            from email.mime.multipart import MIMEMultipart as formatodoemail
                            from email.mime.text import MIMEText as textodoemail
                            import smtplib

                            conectar = smtplib.SMTP("smtp-mail.outlook.com",587) #Conecta ao servidor
                            conectar.starttls() #Transporte layer security
                            conectar.login(f"{email_}", f"{senha_}") #Realiza o login

                            mensagem = formatodoemail()
                            HTML = f"""
                            <body>
                            <div style="height:200px;">
                            <center>
                            <div style="background-image: url(https://i.imgur.com/9xFUPqn.png); width: 294px; height: 85px;margin-top: 40px;margin-left:-25px;"></div></center>
                            <p style="color: #2887bf;text-align: center;font-size: 14px;padding-top: 25px;font-weight: bold;letter-spacing: 10px;">AVISO</p>
                            </div>
                            <div style="text-align: center;">
                            <h1>Olá, {nome_do_paciente}!</h1>
                            <h2 style="font-size: 20px;">Infelizmente a sua consulta do dia <div style="display: inline-block;color: #4a66a2;text-decoration: underline;">{data}</div> precisou ser <div style="display: inline-block;color: red;">cancelada</div>.</h2>
                            <div style="border: 1px solid silver;padding: 10px;border-radius: 10px;">
                            <div style="border-bottom: 1px solid silver;">

                            <div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Endereço:<div style="display: inline;font-weight: bold;margin-left: 5px;">{endereco}</div></div></div>
                            <div style="border-bottom: 1px solid silver;"><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;"> Horário: <div style="display: inline;font-weight: bold;margin-left: 5px;">{horario}</div></div>

                            </div>
                            <div style=""><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Profissional:<div style="display: inline;font-weight: bold;margin-left: 5px;">{profissional}</div></div>

                            </div>
                            </div>


                            <div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">WhatsApp: ({ddd}) {whatsapp}</div><div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">E-mail: {contato}</div>

                            <p>Em caso de dúvidas ou reagendamento entre em contato conosco pelos nossos canais de comunicação.</p>
                            <p>Nós agradecemos pela compreensão :)</p>
                            <p>Equipe {nome}</p><p style="font-size: 12px;margin-top: 50px;color: silver;">E-MAIL ENVIADO AUTOMATICAMENTE. POR FAVOR, NÃO RESPONDER</p></div>
                            </body>
                            """
                            mensagem['Subject'] = f"AVISO - {nome}" #Assunto do e-mail
                            mensagem.attach(textodoemail(HTML,'html')) #Conteúdo do texto//Lê em formato HTML
                            texto = mensagem.as_string() #Coloca como string

                            conectar.sendmail(f"{email_}",email_do_paciente,texto) #Envia o e-mail
                            conectar.close()
                            funcao_aviso("emailsucesso")
                        except:
                            funcao_aviso("erro")
                else:
                    funcao_aviso("erro")
                    
            #Botão cancelar
            self.botao_cancelar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_cancelar.setGeometry(QtCore.QRect(90, 630, 41, 31))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_cancelar.setFont(font)
            self.botao_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_cancelar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_cancelar.setText("")
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("midia/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botao_cancelar.setIcon(icon3)
            self.botao_cancelar.setIconSize(QtCore.QSize(31, 31))
            self.botao_cancelar.setObjectName("botao_cancelar")
            self.botao_cancelar.clicked.connect(lambda: funcao_enviar_email_cancelamento())

            #Função de edição
            def funcao_editar():
                if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                    linha_tb = self.tableWidget.currentItem()
                    if linha_tb != None:
                        linha_tb = self.tableWidget.currentItem().row()
                        linha_tb = int(linha_tb)
                        pago_ = self.tableWidget.item(linha_tb,0).text().upper()
                        paciente_ = self.tableWidget.item(linha_tb,1).text().upper()
                        responsavel_ = self.tableWidget.item(linha_tb,3).text().upper()
                        profissional_ = self.tableWidget.item(linha_tb,4).text().upper()
                        horario_ = self.tableWidget.item(linha_tb,5).text().upper()
                        data_ = self.tableWidget.item(linha_tb,6).text()
                        celular_ = self.tableWidget.item(linha_tb,7).text()
                        valor_ = self.tableWidget.item(linha_tb,8).text()
                        email_ = self.tableWidget.item(linha_tb,9).text()
                        laudo_ = self.tableWidget.item(linha_tb,10).text()
                        endereco_ = str(self.tableWidget.item(linha_tb,11).text())
                        observacoes_ = self.tableWidget.item(linha_tb,12).text()
                        id_ = int(self.tableWidget.item(linha_tb,13).text())
                        import sqlite3
                        from sqlite3 import Error
                        from config import conexao, manipulador
                        manipulador.execute(f"UPDATE consultas_db SET pago = '{pago_}', paciente = '{paciente_}', responsavel = '{responsavel_}', profissional_r = '{profissional_}', horario = '{horario_}', data = '{data_}', celular = '{celular_}', valor = '{valor_}', email = '{email_}', laudo = '{laudo_}', endereco = '{endereco_}', observacoes = '{observacoes_}' WHERE id = {id_}")
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
                        manipulador.execute(f"UPDATE consultas_db SET apagado = 's' WHERE id = {id_}")
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
                                planilha.create_sheet(index = 0, title = "Consultas")
                                folha = planilha["Consultas"]
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
                                        
                                    if listdir(pasta_clinicdata) == [] or "consultas.xlsx" not in listdir(pasta_clinicdata):
                                        nome = "consultas.xlsx"
                                    else:
                                        numero = 1
                                        for k in range(0,len(listdir(pasta_clinicdata))):
                                            nome = str("consultas" + "(" + str(numero) + ")" + ".xlsx")
                                            if nome in listdir(pasta_clinicdata):
                                                numero +=1
                                    planilha.save(pasta_clinicdata + "\\" + nome)#Salva a planilha na pasta
                                else: #Para salvar nos outros sistemas
                                    planilha.save("consultas.xlsx")#Salva a planilha na pasta
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
                        manipulador.execute(f'SELECT * FROM consultas_db WHERE codigo LIKE "%{pesquisar}%"')
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
                        manipulador.execute(f'SELECT * FROM consultas_db WHERE paciente LIKE "%{pesquisar}%"')
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

        #Final padrão
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
