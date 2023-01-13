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
        self.texto_boasvindas.setText("Novo profissional")

        try:
            manipulador.execute('SELECT * FROM log_db')
            entrada = list(manipulador.fetchone())
            conexao.commit()
            
            #Label - Senha
            self.texto_senha = QtWidgets.QLabel(self.centralwidget)
            self.texto_senha.setGeometry(QtCore.QRect(600, 80, 55, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_senha.setFont(font)
            self.texto_senha.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_senha.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_senha.setObjectName("texto_senha")
            self.texto_senha.setText("Senha")
            
            #Label - E-mail
            self.texto_usuario = QtWidgets.QLabel(self.centralwidget)
            self.texto_usuario.setGeometry(QtCore.QRect(430, 170, 61, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_usuario.setFont(font)
            self.texto_usuario.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_usuario.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_usuario.setObjectName("texto_usuario")
            self.texto_usuario.setText("Usuário")
            
            #Label - Cargo
            self.texto_area = QtWidgets.QLabel(self.centralwidget)
            self.texto_area.setGeometry(QtCore.QRect(775, 170, 45, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_area.setFont(font)
            self.texto_area.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_area.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_area.setObjectName("texto_area")
            self.texto_area.setText("Área")

            #Label - E-mail
            self.texto_email = QtWidgets.QLabel(self.centralwidget)
            self.texto_email.setGeometry(QtCore.QRect(50, 170, 55, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_email.setFont(font)
            self.texto_email.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_email.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_email.setObjectName("texto_email")
            self.texto_email.setText("E-mail")
            
            #Label - Nome
            self.texto_nome = QtWidgets.QLabel(self.centralwidget)
            self.texto_nome.setGeometry(QtCore.QRect(50, 80, 48, 20))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.texto_nome.setFont(font)
            self.texto_nome.setStyleSheet("background: white; color: #A6A6A6;")
            self.texto_nome.setAlignment(QtCore.Qt.AlignCenter)
            self.texto_nome.setObjectName("texto_nome")
            self.texto_nome.setText("Nome")

            #Label - Erro
            self.texto_erro = QtWidgets.QLabel(self.centralwidget)
            self.texto_erro.setGeometry(QtCore.QRect(30, 630, 218, 16))
            self.texto_erro.setStyleSheet("color: #ED8686;")
            self.texto_erro.setObjectName("texto_erro")

            #Label - Sucesso
            self.texto_sucesso = QtWidgets.QLabel(self.centralwidget)
            self.texto_sucesso.setGeometry(QtCore.QRect(30, 630, 218, 16))
            self.texto_sucesso.setStyleSheet("color: #2887BF;")
            self.texto_sucesso.setObjectName("texto_sucesso")
            
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

            #Função limpar
            def funcao_limpar():
                self.input.setText("")
                self.input_2.setText("")
                self.input_3.setText("")
                self.input_4.setText("")
                self.input_5.setText("")
                self.texto_erro.setText("")
                self.texto_sucesso.setText("")
                    
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
            self.botao_limpar.clicked.connect(lambda: funcao_limpar())
            
            #Função para enviar
            def funcao_enviar():
                self.texto_erro.raise_()
                nome = str(self.input.text()).upper()
                senha = str(self.input_2.text())
                email = str(self.input_3.text())
                usuario = str(self.input_4.text()).lower()
                area = str(self.input_5.text()).upper()

                if senha == '' or nome == '' or usuario == '' or email == '':
                    self.texto_sucesso.setText("")
                    self.texto_erro.setText("Preencha todos os campos.")
                elif senha != '' and (len(senha) < 8):
                    self.texto_sucesso.setText("")
                    self.texto_erro.setText("Sua senha precisa ter no mínimo 8 caracteres.")
                else:
                    manipulador.execute(f'SELECT COUNT(*) FROM administradores WHERE usuario = "{usuario}"')
                    num = list(manipulador.fetchone())
                    num = num[0]
                    if num != 0:
                        self.texto_sucesso.setText("")
                        self.texto_erro.setText("Usuário já existente. Tente outro.")
                    else:
                        manipulador.execute(f'INSERT INTO administradores(nome,senha,email,usuario,funcao) VALUES("{nome}","{senha}","{email}","{usuario}","PROFISSIONAL")')
                        conexao.commit()
                        manipulador.execute(f'INSERT INTO profissionais(nome,usuario,area) VALUES("{nome}","{usuario}","{area}")')
                        conexao.commit()
                        self.texto_erro.setText("")
                        self.texto_sucesso.raise_()
                        self.texto_sucesso.setText("Enviado com sucesso.")
                            
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
            self.botao_enviar.clicked.connect(lambda: funcao_enviar())
            
            #Final - Padrão PyQt
            self.texto_nome.raise_()
            self.texto_email.raise_()
            self.texto_senha.raise_()
            self.texto_usuario.raise_()
            self.texto_area.raise_()
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
