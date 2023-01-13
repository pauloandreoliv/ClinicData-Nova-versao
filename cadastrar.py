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

        #Barra inicial
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

        #Label - Boas vindas
        self.texto_boasvindas = QtWidgets.QLabel(self.widget)
        self.texto_boasvindas.setGeometry(QtCore.QRect(20, 8, 731, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.texto_boasvindas.setFont(font)
        self.texto_boasvindas.setStyleSheet("color: white;")
        self.texto_boasvindas.setObjectName("texto_boasvindas")
        self.texto_boasvindas.setText("Cadastrar paciente")
        
        try:
            manipulador.execute('SELECT * FROM log_db')
            entrada = list(manipulador.fetchone())
            conexao.commit()
            
            #Label - Responsável
            self.texto_responsavel = QtWidgets.QLabel(self.centralwidget)
            self.texto_responsavel.setGeometry(QtCore.QRect(600, 80, 101, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_responsavel.setFont(font)
            self.texto_responsavel.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_responsavel.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_responsavel.setObjectName("texto_responsavel")
            self.texto_responsavel.setText("Responsável")
            
            #Label - Celular
            self.texto_celular = QtWidgets.QLabel(self.centralwidget)
            self.texto_celular.setGeometry(QtCore.QRect(430, 170, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_celular.setFont(font)
            self.texto_celular.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_celular.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_celular.setObjectName("texto_celular")
            self.texto_celular.setText("Celular")
            
            #Label - CPF
            self.texto_cpf = QtWidgets.QLabel(self.centralwidget)
            self.texto_cpf.setGeometry(QtCore.QRect(780, 170, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_cpf.setFont(font)
            self.texto_cpf.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_cpf.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_cpf.setObjectName("texto_cpf")
            self.texto_cpf.setText("CPF")
            
            #Label - Profissional
            self.texto_profissional = QtWidgets.QLabel(self.centralwidget)
            self.texto_profissional.setGeometry(QtCore.QRect(50, 260, 81, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_profissional.setFont(font)
            self.texto_profissional.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_profissional.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_profissional.setObjectName("texto_profissional")
            self.texto_profissional.setText("Profissional")
            
            #Label - Escola
            self.texto_escola = QtWidgets.QLabel(self.centralwidget)
            self.texto_escola.setGeometry(QtCore.QRect(430, 260, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_escola.setFont(font)
            self.texto_escola.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_escola.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_escola.setObjectName("texto_escola")
            self.texto_escola.setText("Escola")

            #Label - Laudo
            self.texto_laudo = QtWidgets.QLabel(self.centralwidget)
            self.texto_laudo.setGeometry(QtCore.QRect(50, 350, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_laudo.setFont(font)
            self.texto_laudo.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_laudo.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_laudo.setObjectName("texto_laudo")
            self.texto_laudo.setText("Laudo")
            
            #Label - Endereço
            self.texto_endereco = QtWidgets.QLabel(self.centralwidget)
            self.texto_endereco.setGeometry(QtCore.QRect(430, 350, 71, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_endereco.setFont(font)
            self.texto_endereco.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_endereco.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_endereco.setObjectName("texto_endereco")
            self.texto_endereco.setText("Endereço")
            
            #Label - Observações
            self.texto_observacoes = QtWidgets.QLabel(self.centralwidget)
            self.texto_observacoes.setGeometry(QtCore.QRect(50, 440, 101, 21))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_observacoes.setFont(font)
            self.texto_observacoes.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_observacoes.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_observacoes.setObjectName("texto_observacoes")
            self.texto_observacoes.setText("Observações")
            
            #Label - Nascimento
            self.texto_nascimento = QtWidgets.QLabel(self.centralwidget)
            self.texto_nascimento.setGeometry(QtCore.QRect(430, 440, 91, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_nascimento.setFont(font)
            self.texto_nascimento.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_nascimento.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_nascimento.setObjectName("texto_nascimento")
            self.texto_nascimento.setText("Nascimento")
            
            #Label - Frequência
            self.texto_frequencia = QtWidgets.QLabel(self.centralwidget)
            self.texto_frequencia.setGeometry(QtCore.QRect(770, 440, 91, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_frequencia.setFont(font)
            self.texto_frequencia.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_frequencia.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_frequencia.setObjectName("texto_frequencia")
            self.texto_frequencia.setText("Frequência")
            
            #Label - Erro
            self.texto_erro = QtWidgets.QLabel(self.centralwidget)
            self.texto_erro.setGeometry(QtCore.QRect(30, 630, 218, 16))
            self.texto_erro.setStyleSheet("color: #ED8686;")
            self.texto_erro.setObjectName("texto_erro")

            #Label - Sucesso
            self.texto_sucesso = QtWidgets.QLabel(self.centralwidget)
            self.texto_sucesso.setGeometry(QtCore.QRect(30, 630, 600, 16))
            self.texto_sucesso.setStyleSheet("color: #2887BF;")
            self.texto_sucesso.setObjectName("texto_sucesso")
            
            #Label - Email
            self.texto_email = QtWidgets.QLabel(self.centralwidget)
            self.texto_email.setGeometry(QtCore.QRect(50, 170, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_email.setFont(font)
            self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_email.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_email.setObjectName("texto_email")
            self.texto_email.setText("*E-mail")
            
            #Label - Paciente
            self.texto_paciente = QtWidgets.QLabel(self.centralwidget)
            self.texto_paciente.setGeometry(QtCore.QRect(50, 80, 71, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_paciente.setFont(font)
            self.texto_paciente.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_paciente.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_paciente.setObjectName("texto_paciente")
            self.texto_paciente.setText("*Paciente")
            
            #Input 1
            self.input = QtWidgets.QLineEdit(self.centralwidget)
            self.input.setGeometry(QtCore.QRect(20, 90, 501, 51))
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
            self.input_2.setGeometry(QtCore.QRect(570, 90, 501, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_2.setFont(font)
            self.input_2.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_2.setAlignment(QtCore.Qt.AlignLeft)
            self.input_2.setObjectName("input_2")

            #Input 3
            self.input_3 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_3.setGeometry(QtCore.QRect(20, 180, 341, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_3.setFont(font)
            self.input_3.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_3.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_3.setAlignment(QtCore.Qt.AlignLeft)
            self.input_3.setObjectName("input_3")

            #Input 4
            self.input_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_4.setGeometry(QtCore.QRect(400, 180, 321, 51))
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
            self.input_5.setGeometry(QtCore.QRect(750, 180, 321, 51))
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
            self.input_6.setGeometry(QtCore.QRect(20, 270, 341, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_6.setFont(font)
            self.input_6.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_6.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_6.setAlignment(QtCore.Qt.AlignLeft)
            self.input_6.setObjectName("input_6")

            #Input 7
            self.input_7 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_7.setGeometry(QtCore.QRect(400, 270, 671, 51))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_7.setFont(font)
            self.input_7.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6;padding: 5px;")
            self.input_7.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.input_7.setAlignment(QtCore.Qt.AlignLeft)
            self.input_7.setObjectName("input_7")

            #Input 8
            self.input_8 = QtWidgets.QLineEdit(self.centralwidget)
            self.input_8.setGeometry(QtCore.QRect(20, 360, 341, 51))
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
            self.input_9.setGeometry(QtCore.QRect(400, 360, 671, 51))
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
            self.input_10.setGeometry(QtCore.QRect(20, 450, 341, 111))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_10.setFont(font)
            self.input_10.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
            self.input_10.setObjectName("input_10")

            #Input 11
            self.input_11 = QtWidgets.QDateEdit(self.centralwidget)
            self.input_11.setGeometry(QtCore.QRect(400, 450, 321, 111))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Segoe UI Light")
            self.input_11.setFont(font)
            self.input_11.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 2px; font-size: 14px;")
            self.input_11.setFrame(True)
            self.input_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.input_11.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 7, 1), QtCore.QTime(0, 0, 0)))
            self.input_11.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
            self.input_11.setCalendarPopup(True)
            self.input_11.setObjectName("input_11")

            #Frame - Frequência
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(740, 450, 321, 111))
            self.frame.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6;")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")

            #Botão - Diária
            self.radioButton = QtWidgets.QRadioButton(self.frame)
            self.radioButton.setGeometry(QtCore.QRect(20, 20, 89, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            self.radioButton.setFont(font)
            self.radioButton.setStyleSheet("border: none;")
            self.radioButton.setObjectName("radioButton")
            self.radioButton.setText("Diária")

            #Botão - Semanal
            self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
            self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 89, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            self.radioButton_2.setFont(font)
            self.radioButton_2.setStyleSheet("border: none;")
            self.radioButton_2.setObjectName("radioButton_2")
            self.radioButton_2.setText("Semanal")

            #Botão - Mensal
            self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
            self.radioButton_3.setGeometry(QtCore.QRect(170, 20, 89, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            self.radioButton_3.setFont(font)
            self.radioButton_3.setStyleSheet("border: none;")
            self.radioButton_3.setObjectName("radioButton_3")
            self.radioButton_3.setText("Mensal")

            #Botão - Outra
            self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
            self.radioButton_4.setGeometry(QtCore.QRect(170, 60, 89, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Light")
            self.radioButton_4.setFont(font)
            self.radioButton_4.setStyleSheet("border: none;")
            self.radioButton_4.setObjectName("radioButton_4")
            self.radioButton_4.setText("Outra")

            #Função limpar
            def funcao_limpar():
                self.input.setText("")
                self.input_2.setText("")
                self.input_3.setText("")
                self.input_4.setText("")
                self.input_5.setText("")
                self.input_6.setText("")
                self.input_7.setText("")
                self.input_8.setText("")
                self.input_9.setText("")
                self.input_10.setText("")
                self.texto_erro.setText("")
                self.texto_sucesso.setText("")
                self.radioButton_4.setChecked(True)
                self.input.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
                self.input_3.setStyleSheet("border: 1px solid silver; border-radius: 10px;color: #A6A6A6; padding: 5px;")
                self.texto_paciente.setStyleSheet("background: white; color: #A6A6A6;")
                self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
                
            #Botão limpar
            self.botao_limpar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_limpar.setGeometry(QtCore.QRect(920, 630, 75, 24))
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(13)
            self.botao_limpar.setFont(font)
            self.botao_limpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_limpar.setStyleSheet("border: none; color: #A6A6A6;")
            self.botao_limpar.setObjectName("botao_limpar")
            self.botao_limpar.setText("Limpar")
            self.botao_limpar.clicked.connect(lambda:funcao_limpar())

            #Função enviar
            def funcao_enviar():
                paciente = str(self.input.text()).upper()
                responsavel = str(self.input_2.text()).upper()
                email = str(self.input_3.text()).upper()
                celular = str(self.input_4.text())
                cpf = str(self.input_5.text())
                profissional = str(self.input_6.text()).upper()
                escola = str(self.input_7.text()).upper()
                laudo = str(self.input_8.text()).upper()
                endereco = str(self.input_9.text()).upper()
                observacoes = str(self.input_10.toPlainText()).upper()
                nascimento = self.input_11.date().toPyDate()
                frequencia = ''
                if self.radioButton.isChecked() == True:
                    frequencia = 'DIÁRIA'
                if self.radioButton_2.isChecked() == True:
                    frequencia = 'SEMANAL'
                if self.radioButton_3.isChecked() == True:
                    frequencia = 'MENSAL'
                if self.radioButton_4.isChecked() == True:
                    frequencia = 'OUTRA'
                if paciente == '' or email == '':
                    self.texto_sucesso.setText("")
                    self.texto_erro.setText("Preencha os campos obrigatórios.")
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
                else:
                    self.texto_erro.setText("")
                    self.texto_sucesso.raise_()
                    manipulador.execute('SELECT codigo FROM pacientes_db')
                    todos_codigos = list(manipulador.fetchall())
                    conexao.commit()
                    codigos_sem_tupla = []
                    for codigo in todos_codigos:
                        codigos_sem_tupla.append(codigo[0])
                    import random
                    caracteres = list(range(0,10))
                    codigo_final = ''
                    while len(codigo_final) < 5:
                        caracter = random.choice(caracteres)
                        codigo_final += str(caracter)
                    if codigo_final in codigos_sem_tupla:
                        funcao_codigo()
                    else:
                        codigo = codigo_final
                    manipulador.execute(f"INSERT INTO pacientes_db (paciente, codigo, responsavel, profissional, nascimento, celular, email, laudo, endereco, observacoes, cpf, nascimento, frequencia, escola) VALUES ('{paciente}', '{codigo}', '{responsavel}', '{profissional}', '{nascimento}', '{celular}', '{email}', '{laudo}', '{endereco}', '{observacoes}', '{cpf}', '{nascimento}', '{frequencia}', '{escola}')")
                    conexao.commit()
                    self.texto_sucesso.setText(f"Enviado com sucesso. O código do paciente é: {codigo}")
            
            #Botão - Enviar
            self.botao_enviar = QtWidgets.QPushButton(self.centralwidget)
            self.botao_enviar.setGeometry(QtCore.QRect(1010, 630, 75, 24))
            font = QtGui.QFont()
            font.setPointSize(13)
            self.botao_enviar.setFont(font)
            self.botao_enviar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_enviar.setStyleSheet("border: none; color: #2887BF;")
            self.botao_enviar.setObjectName("botao_enviar")
            self.botao_enviar.setText("Enviar")
            self.botao_enviar.clicked.connect(lambda:funcao_enviar())
            
            #Final - Padrão PyQt
            self.texto_paciente.raise_()
            self.texto_email.raise_()
            self.texto_responsavel.raise_()
            self.texto_celular.raise_()
            self.texto_cpf.raise_()
            self.texto_profissional.raise_()
            self.texto_escola.raise_()
            self.texto_laudo.raise_()
            self.texto_endereco.raise_()
            self.texto_observacoes.raise_()
            self.texto_nascimento.raise_()
            self.texto_frequencia.raise_()
            self.texto_erro.raise_()

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
