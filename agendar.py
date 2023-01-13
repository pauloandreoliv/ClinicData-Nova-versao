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
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        ClinicData.setFont(font)
        
        #Label - Boas-vindas 
        self.texto_boasvindas = QtWidgets.QLabel(self.centralwidget)
        self.texto_boasvindas.setGeometry(QtCore.QRect(20, 8, 731, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.texto_boasvindas.setFont(font)
        self.texto_boasvindas.setStyleSheet("color: white; background: transparent;")
        self.texto_boasvindas.setObjectName("texto_boasvindas")
        self.texto_boasvindas.setText("Agendar consulta")

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
            
            #Label - Paciente
            self.texto_paciente = QtWidgets.QLabel(self.centralwidget)
            self.texto_paciente.setGeometry(QtCore.QRect(50, 170, 71, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_paciente.setFont(font)
            self.texto_paciente.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_paciente.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_paciente.setObjectName("texto_paciente")
            self.texto_paciente.setText("*Paciente")

            #Label - E-mail
            self.texto_email = QtWidgets.QLabel(self.centralwidget)
            self.texto_email.setGeometry(QtCore.QRect(50, 250, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_email.setFont(font)
            self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_email.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_email.setObjectName("texto_email")
            self.texto_email.setText("*E-mail")
            
            #Label - Responsável
            self.texto_responsavel = QtWidgets.QLabel(self.centralwidget)
            self.texto_responsavel.setGeometry(QtCore.QRect(600, 170, 101, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_responsavel.setFont(font)
            self.texto_responsavel.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_responsavel.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_responsavel.setObjectName("texto_responsavel")
            self.texto_responsavel.setText("Responsável")
            
            #Label - Celular
            self.texto_celular = QtWidgets.QLabel(self.centralwidget)
            self.texto_celular.setGeometry(QtCore.QRect(430, 250, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_celular.setFont(font)
            self.texto_celular.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_celular.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_celular.setObjectName("texto_celular")
            self.texto_celular.setText("Celular")
            
            #Label - Valor
            self.texto_valor = QtWidgets.QLabel(self.centralwidget)
            self.texto_valor.setGeometry(QtCore.QRect(780, 250, 41, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_valor.setFont(font)
            self.texto_valor.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_valor.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_valor.setObjectName("texto_valor")
            self.texto_valor.setText("Valor")
            
            #Label - Laudo
            self.texto_laudo = QtWidgets.QLabel(self.centralwidget)
            self.texto_laudo.setGeometry(QtCore.QRect(50, 330, 51, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_laudo.setFont(font)
            self.texto_laudo.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_laudo.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_laudo.setObjectName("texto_laudo")
            self.texto_laudo.setText("Laudo")
            
            #Label - Profissional
            self.texto_profissional = QtWidgets.QLabel(self.centralwidget)
            self.texto_profissional.setGeometry(QtCore.QRect(430, 330, 81, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_profissional.setFont(font)
            self.texto_profissional.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_profissional.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_profissional.setObjectName("texto_profissional")
            self.texto_profissional.setText("Profissional")
            
            #Label - Hora
            self.texto_hora = QtWidgets.QLabel(self.centralwidget)
            self.texto_hora.setGeometry(QtCore.QRect(50, 410, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_hora.setFont(font)
            self.texto_hora.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_hora.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_hora.setObjectName("texto_hora")
            self.texto_hora.setText("Hora")
            
            #Label - Endereço
            self.texto_endereco = QtWidgets.QLabel(self.centralwidget)
            self.texto_endereco.setGeometry(QtCore.QRect(430, 410, 71, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_endereco.setFont(font)
            self.texto_endereco.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_endereco.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_endereco.setObjectName("texto_endereco")
            self.texto_endereco.setText("Endereço")
            
            #Label - Observações
            self.texto_observacoes = QtWidgets.QLabel(self.centralwidget)
            self.texto_observacoes.setGeometry(QtCore.QRect(50, 490, 101, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_observacoes.setFont(font)
            self.texto_observacoes.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_observacoes.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_observacoes.setObjectName("texto_observacoes")
            self.texto_observacoes.setText("Observações")
            
            #Label - Data
            self.texto_data = QtWidgets.QLabel(self.centralwidget)
            self.texto_data.setGeometry(QtCore.QRect(430, 490, 41, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_data.setFont(font)
            self.texto_data.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_data.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_data.setObjectName("texto_data")
            self.texto_data.setText("Data")

            #Label - Pago
            self.texto_pago = QtWidgets.QLabel(self.centralwidget)
            self.texto_pago.setGeometry(QtCore.QRect(770, 480, 41, 31))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_pago.setFont(font)
            self.texto_pago.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_pago.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_pago.setObjectName("texto_pago")
            self.texto_pago.setText("Pago")

            #Label - Erro
            self.texto_erro = QtWidgets.QLabel(self.centralwidget)
            self.texto_erro.setGeometry(QtCore.QRect(30, 630, 211, 16))
            self.texto_erro.setStyleSheet("color: #ED8686;")
            self.texto_erro.setObjectName("texto_erro")

            #Label - Pesquisar código
            self.texto_pesquisar = QtWidgets.QLabel(self.centralwidget)
            self.texto_pesquisar.setGeometry(QtCore.QRect(50, 80, 121, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_pesquisar.setFont(font)
            self.texto_pesquisar.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_pesquisar.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_pesquisar.setObjectName("texto_pesquisar")
            self.texto_pesquisar.setText("Pesquisar código")
            
            #Label - Erro ao pesquisar
            self.texto_erro_2 = QtWidgets.QLabel(self.centralwidget)
            self.texto_erro_2.setGeometry(QtCore.QRect(20, 150, 471, 16))
            self.texto_erro_2.setStyleSheet("color: #ED8686;")
            self.texto_erro_2.setObjectName("texto_erro_2")

            #Label - Sucesso
            self.texto_sucesso = QtWidgets.QLabel(self.centralwidget)
            self.texto_sucesso.setGeometry(QtCore.QRect(30, 630, 211, 16))
            self.texto_sucesso.setStyleSheet("color: #2887BF;")
            self.texto_sucesso.setObjectName("texto_sucesso")
            
            #Input 1
            self.input = QtWidgets.QLineEdit(self.centralwidget)
            self.input.setGeometry(QtCore.QRect(20, 180, 501, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input.setFont(font)
            self.input.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input.setText("")
            self.input.setAlignment(QtCore.Qt.AlignLeft)
            self.input.setObjectName("input")

            #Input 2
            self.input_2 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_2.setGeometry(QtCore.QRect(570, 180, 501, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_2.setFont(font)
            self.input_2.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_2.setAlignment(QtCore.Qt.AlignLeft)
            self.input_2.setObjectName("input_2")
            
            #Input 3
            self.input_3 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_3.setGeometry(QtCore.QRect(20, 260, 341, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_3.setFont(font)
            self.input_3.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6;padding: 5px;")
            self.input_3.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_3.setAlignment(QtCore.Qt.AlignLeft)
            self.input_3.setObjectName("input_3")

            #Input 4
            self.input_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_4.setGeometry(QtCore.QRect(400, 260, 321, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_4.setFont(font)
            self.input_4.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_4.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_4.setAlignment(QtCore.Qt.AlignLeft)
            self.input_4.setObjectName("input_4")

            #Input 5
            self.input_5 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_5.setGeometry(QtCore.QRect(750, 260, 321, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_5.setFont(font)
            self.input_5.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_5.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_5.setAlignment(QtCore.Qt.AlignLeft)
            self.input_5.setObjectName("input_5")

            #Input 6
            self.input_6 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_6.setGeometry(QtCore.QRect(20, 340, 341, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_6.setFont(font)
            self.input_6.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_6.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_6.setAlignment(QtCore.Qt.AlignLeft)
            self.input_6.setObjectName("input_6")

            #Input 7
            manipulador.execute('SELECT funcao, nome FROM log_db')
            funcao = list(manipulador.fetchone())
            conexao.commit() 
            if funcao[0] != 'RECEPÇÃO/ADMINISTRAÇÃO':
                self.input_7 = QtWidgets.QLineEdit(self.centralwidget)
                self.input_7.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.input_7.setAlignment(QtCore.Qt.AlignLeft)
                self.input_7.setText(f"{funcao[1]}")
                input_ = True
            else:
                self.input_7 = QtWidgets.QComboBox(self.centralwidget)
                manipulador.execute('SELECT nome FROM profissionais')
                profissionais = list(manipulador.fetchall())
                input_ = False
                cont = 0
                while cont < len(profissionais):
                    self.input_7.addItem("")
                    cont+=1
                    
                cont2 = 0
                while cont2 < len(profissionais):
                    self.input_7.setItemText(cont2, f"{profissionais[cont2][0]}")
                    cont2+=1
            self.input_7.setGeometry(QtCore.QRect(400, 340, 671, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_7.setFont(font)
            self.input_7.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_7.setObjectName("input_7")

            #Input 8
            self.input_8 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_8.setGeometry(QtCore.QRect(20, 420, 341, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_8.setFont(font)
            self.input_8.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_8.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_8.setAlignment(QtCore.Qt.AlignLeft)
            self.input_8.setObjectName("input_8")

            #Input 9
            self.input_9 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_9.setGeometry(QtCore.QRect(400, 420, 671, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_9.setFont(font)
            self.input_9.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_9.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_9.setAlignment(QtCore.Qt.AlignLeft)
            self.input_9.setObjectName("input_9")

            #Input 10
            self.input_10 = QtWidgets.QTextEdit(self.centralwidget)
            self.input_10.setGeometry(QtCore.QRect(20, 500, 341, 111))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_10.setFont(font)
            self.input_10.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_10.setObjectName("input_10")

            #Input 11
            self.input_11 = QtWidgets.QDateEdit(self.centralwidget)
            self.input_11.setGeometry(QtCore.QRect(400, 500, 321, 111))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_11.setFont(font)
            self.input_11.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 2px; font-size: 18px;")
            self.input_11.setFrame(True)
            self.input_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.input_11.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 7, 1), QtCore.QTime(0, 0, 0)))
            self.input_11.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 7, 1), QtCore.QTime(0, 0, 0)))
            self.input_11.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
            self.input_11.setCalendarPopup(True)
            self.input_11.setObjectName("input_11")

            #Input 12
            self.input_12 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_12.setGeometry(QtCore.QRect(20, 90, 1009, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_12.setFont(font)
            self.input_12.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_12.setText("")
            self.input_12.setAlignment(QtCore.Qt.AlignLeft)
            self.input_12.setClearButtonEnabled(False)
            self.input_12.setObjectName("input_12")
            
            #Frame - Pago
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(740, 500, 321, 111))
            self.frame.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6;")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")

            #Botão - Sim
            self.radioButton = QtWidgets.QRadioButton(self.frame)
            self.radioButton.setGeometry(QtCore.QRect(40, 50, 89, 20))
            font = QtGui.QFont()
            self.radioButton.setFont(font)
            self.radioButton.setStyleSheet("border: none;")
            self.radioButton.setObjectName("radioButton")
            self.radioButton.setText("Sim")

            #Botão - Não
            self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
            self.radioButton_2.setGeometry(QtCore.QRect(190, 50, 89, 20))
            font = QtGui.QFont()
            self.radioButton_2.setFont(font)
            self.radioButton_2.setStyleSheet("border: none;")
            self.radioButton_2.setObjectName("radioButton_2")
            self.radioButton_2.setText("Não")

            #Função para pesquisar
            def funcao_pesquisar():
                pesquisar = str(self.input_12.text())
                str_ou_int = pesquisar.isdigit()
                if pesquisar == '':
                    self.texto_erro_2.setText("Digite um código de paciente.")
                else:
                    try:
                        if str_ou_int == True:
                            manipulador.execute(f'SELECT paciente, responsavel, email, celular, laudo, endereco, observacoes FROM pacientes_db WHERE codigo = {pesquisar}')
                            paciente = list(manipulador.fetchone())
                            self.input.setText(f"{paciente[0]}")
                            self.input_2.setText(f"{paciente[1]}")
                            self.input_3.setText(f"{paciente[2]}")
                            self.input_4.setText(f"{paciente[3]}")
                            self.input_6.setText(f"{paciente[4]}")
                            self.input_9.setText(f"{paciente[5]}")
                            self.input_10.setText(f"{paciente[6]}")
                    except:
                        self.texto_erro_2.setText("Código inexistente ou incorreto. Por favor, verifique o código informado")
            
            #Botão pesquisar
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(1033, 90, 41, 51))
            self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton.setStyleSheet("border: none;")
            self.pushButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("midia/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(25, 25))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(lambda: funcao_pesquisar())

            #Função para enviar
            def funcao_enviar():
                paciente = str(self.input.text()).upper()
                responsavel = str(self.input_2.text()).upper()
                email = str(self.input_3.text()).upper()
                celular = str(self.input_4.text())
                valor = str(self.input_5.text())
                laudo = str(self.input_6.text()).upper()
                if input_ == True:
                    profissional = str(self.input_7.text()).upper()
                else:
                    profissional = str(self.input_7.currentText()).upper()
                horario = str(self.input_8.text())
                endereco = str(self.input_9.text()).upper()
                observacoes = str(self.input_10.toPlainText()).upper()
                data = self.input_11.date().toPyDate()
                erro = False
                if paciente == '' or email == '':
                    self.texto_erro.setText("Preencha os campos obrigatórios.")
                    erro = True
                else:
                    self.texto_erro.setText("")
                if paciente == '':
                    self.texto_paciente.setStyleSheet("background: white; color: #ED8686;")
                    self.input.setStyleSheet("border: 1px solid #ED8686; border-radius: 10px; color: #ED8686; padding: 5px;")
                else:
                    self.texto_paciente.setStyleSheet("background: white; color: #A6A6A6;")
                    self.input.setStyleSheet("border: 1px solid silver; border-radius: 10px; color: #A6A6A6; padding: 5px;")
                if email == '':
                    self.texto_email.setStyleSheet("background: white; color: #ED8686;")
                    self.input_3.setStyleSheet("border: 1px solid #ED8686; border-radius: 10px; color: #ED8686; padding: 5px;")
                else:
                    self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
                    self.input_3.setStyleSheet("border: 1px solid silver; border-radius: 10px; color: #A6A6A6; padding: 5px;")
                pago = ''
                if self.radioButton.isChecked() == True:
                    pago = 'SIM'
                if self.radioButton_2.isChecked() == True:
                    pago = 'NÃO'
                if erro == False:
                    self.texto_erro.setText("")
                    manipulador.execute(f"INSERT INTO consultas_db (pago, paciente, responsavel, profissional_r, data, celular, valor, email, laudo, endereco, observacoes, horario, apagado) VALUES ('{pago}', '{paciente}', '{responsavel}', '{profissional}', '{data}', '{celular}', '{valor}', '{email}', '{laudo}', '{endereco}', '{observacoes}', '{horario}', 'n')")
                    conexao.commit()
                    self.texto_sucesso.raise_()
                    self.texto_sucesso.setText("Enviado com sucesso")
                
            #Botão enviar
            self.botao_enviar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_enviar.setGeometry(QtCore.QRect(1010, 630, 75, 24))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_enviar.setFont(font)
            self.botao_enviar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_enviar.setStyleSheet("border: none; color: #2887BF;")
            self.botao_enviar.setObjectName("botao_enviar")
            self.botao_enviar.setText("Enviar")
            self.botao_enviar.clicked.connect(lambda: funcao_enviar())

            #Função limpar
            def funcao_limpar():
                self.input.setText("")
                self.input_2.setText("")
                self.input_3.setText("")
                self.input_4.setText("")
                self.input_5.setText("")
                self.input_6.setText("")
                self.input_8.setText("")
                self.input_9.setText("")
                self.input_10.setText("")
                self.input_12.setText("")
                self.radioButton_2.setChecked(True)
                self.texto_paciente.setStyleSheet("background: white; color: #A6A6A6;")
                self.input.setStyleSheet("border: 1px solid silver; border-radius: 10px; color: #A6A6A6; padding: 5px;")
                self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
                self.input_3.setStyleSheet("border: 1px solid silver; border-radius: 10px; color: #A6A6A6; padding: 5px;")
                self.texto_erro.setText("")
                self.texto_erro_2.setText("")
                self.texto_sucesso.setText("")
                
            #Botão limpar
            self.botao_limpar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_limpar.setGeometry(QtCore.QRect(920, 630, 75, 24))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_limpar.setFont(font)
            self.botao_limpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_limpar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_limpar.setObjectName("botao_limpar")
            self.botao_limpar.setText("Limpar")
            self.botao_limpar.clicked.connect(lambda: funcao_limpar())
            
            #Final - Padrão PyQt
            self.frame.raise_()
            self.texto_paciente.raise_()
            self.botao_enviar.raise_()
            self.widget.raise_()
            self.texto_email.raise_()
            self.texto_responsavel.raise_()
            self.texto_celular.raise_()
            self.texto_valor.raise_()
            self.texto_laudo.raise_()
            self.texto_profissional.raise_()
            self.texto_hora.raise_()
            self.texto_endereco.raise_()
            self.texto_observacoes.raise_()
            self.texto_data.raise_()
            self.texto_pago.raise_()
            self.texto_erro.raise_()
            self.texto_pesquisar.raise_()
            self.texto_erro_2.raise_()
            self.texto_boasvindas.raise_()
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
