from config import *

class Ui_ClinicData_Login(object):
    def setupUi(self, ClinicData_Login):

        #Propriedades
        ClinicData_Login.setObjectName("ClinicData_Login")
        ClinicData_Login.resize(1120, 680)
        ClinicData_Login.setMaximumSize(QtCore.QSize(1120, 680))
        ClinicData_Login.setStyleSheet("background-color: white;")
        ClinicData_Login.setWindowTitle("ClinicData")
        self.centralwidget = QtWidgets.QWidget(ClinicData_Login)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        ClinicData_Login.setFont(font)

        #Imagem
        self.img_inicial = QtWidgets.QLabel(self.centralwidget)
        self.img_inicial.setGeometry(QtCore.QRect(-10, 120, 671, 491))
        self.img_inicial.setText("")
        self.img_inicial.setPixmap(QtGui.QPixmap("midia/img_inicial.png"))
        self.img_inicial.setObjectName("img_inicial")

        #Logo
        self.logo_inicial = QtWidgets.QLabel(self.centralwidget)
        self.logo_inicial.setGeometry(QtCore.QRect(720, 160, 391, 121))
        self.logo_inicial.setText("")
        self.logo_inicial.setPixmap(QtGui.QPixmap("midia/logo_inicial.png"))
        self.logo_inicial.setObjectName("logo_inicial")
        
        #Input usuário
        self.usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(700, 300, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.usuario.setStyleSheet("border: 1px solid silver; padding: 5px; border-radius: 10px;color: #A6A6A6;")
        self.usuario.setAlignment(QtCore.Qt.AlignLeft)
        self.usuario.setObjectName("usuario")
        
        #Input senha
        self.senha = QtWidgets.QLineEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(700, 400, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.senha.setStyleSheet("border: 1px solid silver; padding: 5px; border-radius: 10px;color: #A6A6A6;")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setAlignment(QtCore.Qt.AlignLeft)
        self.senha.setObjectName("senha")
        
        #Label - Usuário
        self.texto_usuario = QtWidgets.QLabel(self.centralwidget)
        self.texto_usuario.setGeometry(QtCore.QRect(730, 290, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.texto_usuario.setFont(font)
        self.texto_usuario.setStyleSheet("background: white; color: #A6A6A6;")
        self.texto_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.texto_usuario.setObjectName("texto_usuario")
        self.texto_usuario.setText("Usuário")
        
        #Label - Senha
        self.texto_senha = QtWidgets.QLabel(self.centralwidget)
        self.texto_senha.setGeometry(QtCore.QRect(730, 390, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.texto_senha.setFont(font)
        self.texto_senha.setStyleSheet("background: white; color: #A6A6A6;")
        self.texto_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.texto_senha.setObjectName("texto_senha")
        self.texto_senha.setText("Senha")

        #Label - Texto de erro
        self.texto_erro = QtWidgets.QLabel(self.centralwidget)
        self.texto_erro.setGeometry(QtCore.QRect(778, 250, 160, 18))
        self.texto_erro.setObjectName("texto_erro")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Segoe UI Light")
        self.texto_erro.setFont(font)

        #Função de login
        def funcao_login():
            usuario = str(self.usuario.text()).lower()
            senha = str(self.senha.text())
            
            if usuario == '' or senha == '':
                self.texto_erro.setText("Preencha o formulário.")
                self.texto_erro.setStyleSheet("color: #ED8686; padding-left:15px;")
                
            else:
                manipulador.execute('SELECT usuario FROM administradores')
                usuarios = list(manipulador.fetchall())
                usuarios2 = []
                
                for k in usuarios:
                    usuarios2.append(k[0])
                conexao.commit()
                
                if usuario in usuarios2:
                    manipulador.execute(f'SELECT senha FROM administradores WHERE usuario = "{usuario}"')
                    senhas = list(manipulador.fetchone())
                    conexao.commit()
                    
                    if senha == str(senhas[0]): 
                        self.texto_erro.setText("Login realizado com sucesso.")
                        self.texto_erro.setStyleSheet("color: #48CFAE;")
                        
                        manipulador.execute(f'DELETE FROM log_db')
                        conexao.commit()
                        
                        manipulador.execute(f'SELECT nome, funcao FROM administradores WHERE usuario = "{usuario}"')
                        dados_com_tupla = list(manipulador.fetchone())
                        dados = []
                        for k in dados_com_tupla:
                            dados.append(k)
                        conexao.commit()
                        
                        manipulador.execute(f'INSERT INTO log_db (nome, funcao, usuario) VALUES ("{dados[0]}", "{dados[1]}", "{usuario}")')
                        conexao.commit()
                        
                        from principal import Ui_ClinicData_Principal
                        from time import sleep
                        self.ClinicData = QtWidgets.QMainWindow()
                        self.clinicdata = Ui_ClinicData_Principal()
                        self.clinicdata.setupUi(self.ClinicData)
                        sleep(2)
                        self.ClinicData.show()
                        sleep(1)
                        ClinicData_Login.hide()
                        
                    else:
                        self.texto_erro.setText("Usuário ou senha incorretos.")
                        self.texto_erro.setStyleSheet("color: #ED8686;")
                else:
                    self.texto_erro.setText("Usuário ou senha incorretos.")
                    self.texto_erro.setStyleSheet("color: #ED8686;")

                
        #Botão de login
        self.botao_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_entrar.setGeometry(QtCore.QRect(820, 500, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(13)
        self.botao_entrar.setFont(font)
        self.botao_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_entrar.setStyleSheet("border: none; color: #2887BF;")
        self.botao_entrar.setObjectName("botao_entrar")
        self.botao_entrar.setText("Entrar")
        self.botao_entrar.clicked.connect(lambda: funcao_login())

        #Botão de ajuda
        self.botao_ajuda = QtWidgets.QPushButton(self.centralwidget)
        self.botao_ajuda.setGeometry(QtCore.QRect(785, 600, 151, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.botao_ajuda.setFont(font)
        self.botao_ajuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_ajuda.setStyleSheet("border: none;  color: #A6A6A6;")
        self.botao_ajuda.setObjectName("botao_ajuda")
        self.botao_ajuda.setText("Precisa de ajuda?")

        #Final - Padrão PyQt
        ClinicData_Login.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ClinicData_Login)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData_Login = QtWidgets.QMainWindow()
    ui = Ui_ClinicData_Login()
    ui.setupUi(ClinicData_Login)
    ClinicData_Login.show()
    sys.exit(app.exec_())
    conexao.close()
