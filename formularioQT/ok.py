from PyQt5 import uic,QtWidgets
import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="2722",
    database="db_cadastro"
)

# def limpar_campos():
#     formulario.lineEdit.clear()
#     formulario.lineEdit_2.clear()
#     formulario.lineEdit_3.clear()
#     formulario.lineEdit_4.clear()
#     formulario.lineEdit_5.clear()
# preco_unit = float(formulario.lineEdit_4.text().replace(',', '.'))

def funcao_principal():
    linha1=formulario.lineEdit.text()
    linha2=formulario.lineEdit_2.text()
    linha3=formulario.lineEdit_3.text()
    linha4=formulario.lineEdit_4.text()
    
    categoria=""
    
    if formulario.radioButton.isChecked():
        print("Unidade")
        categoria="Unidade"
    elif formulario.radioButton_2.isChecked():
        print("Jogo")
        categoria="Jogo"
    elif formulario.radioButton_3.isChecked():
        print("Par")
        categoria="Par"

    print("Codigo:",linha1)
    print("Descricao:",linha2)
    print("Preco:",linha3)
    print("Estoque:",linha4)
    
    cursor = db.cursor()
    comando_sql = "INSERT INTO cadastro (codigo, descricao, preco, estoque, categoria) VALUES (%s, %s, %s, %s, %s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),categoria)
    cursor.execute(comando_sql,dados)
    db.commit()
    cursor.close()
    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

