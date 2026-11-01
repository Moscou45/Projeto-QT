from PyQt5 import uic, QtWidgets
import pymysql 
import sys



# Configuração da conexão com o banco de dados
def conectar_banco():
    try:
        conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="2722",
            database="db_cadastro",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def excluir_dados():
    linha_selecionada = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha_selecionada)
    
    cursor = conectar_banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    print(f"Linha {linha_selecionada} excluida com sucesso!")    

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    
    categoria = ""
    if formulario.radioButton.isChecked():
        categoria = "Unidade"
    elif formulario.radioButton_2.isChecked():
        categoria = "Jogo"
    elif formulario.radioButton_3.isChecked():
        categoria = "Par"

    print(f"Salvando: {linha2} | Categoria: {categoria}")
    
    db = conectar_banco()
    if db:
        try:
            with db.cursor() as cursor:
                comando_sql = "INSERT INTO cadastro (codigo, descricao, preco, estoque, categoria) VALUES (%s, %s, %s, %s, %s)"
                dados = (str(linha1), str(linha2), str(linha3), str(linha4), categoria)
                cursor.execute(comando_sql, dados)
                db.commit()
                formulario.lineEdit.setText("")
                formulario.lineEdit_2.setText("")
                formulario.lineEdit_3.setText("")
                formulario.lineEdit_4.setText("")
                #formulario.lineEdit_5.setText("") 
                print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            db.close()
         
def chamar_segunda_tela():
 segunda_tela.show()
   
 conexao = conectar_banco()
 if conexao:
    try:
        with conexao.cursor() as cursor:
         comando_sql = "SELECT * FROM cadastro"
         cursor.execute(comando_sql)
         dados_lidos = cursor.fetchall()


         segunda_tela.tableWidget.setRowCount(len(dados_lidos))
         segunda_tela.tableWidget.setColumnCount(6)
         
        #  for i in range(0, len(dados_lidos)):
        #      for j in range(0,6):
        #          segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
         
         for i, linha in enumerate(dados_lidos):
             segunda_tela.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(linha['id'])))
             segunda_tela.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(linha['codigo'])))
             segunda_tela.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(linha['descricao'])))
             segunda_tela.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(linha['preco'])))
             segunda_tela.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(linha['estoque'])))
             segunda_tela.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(linha['categoria'])))
             
         
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
    finally:
        conexao.close()
    

# Inicialização da Interface
app = QtWidgets.QApplication(sys.argv)
formulario = uic.loadUi("formularioQT/formulario.ui")
segunda_tela = uic.loadUi("formularioQT/listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chamar_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_dados)

formulario.show()
sys.exit(app.exec_())