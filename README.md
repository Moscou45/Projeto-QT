# Projeto-QT
Sistema de gestão e registo de inventário/produtos para ambiente de trabalho com interface gráfica em PyQt5 e integração com base de dados MySQL.

# 📦 Sistema de Cadastro e Gestão de Produtos

Aplicação desktop desenvolvida em **Python** e **PyQt5** para registo, consulta e gestão de inventário de peças e produtos, persistindo as informações diretamente numa base de dados relacional **MySQL**.

---

## 🚀 Funcionalidades

- **Registo Completo de Produtos:**
  - Código do produto
  - Descrição detalhada
  - Preço
  - Quantidade em stock
  - Categorização por formato (Unidade, Jogo, Par) através de radio buttons
- **Consulta e Listagem de Inventário:**
  - Visualização em grelha interativa com IDs e códigos associados
- **Gestão de Dados:**
  - Remoção e exclusão de registos selecionados da base de dados
- **Persistência Confiável:**
  - Conexão e sincronização direta com o MySQL através de `PyMySQL`

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Interface Gráfica (GUI):** [PyQt5](https://riverbankcomputing.com/software/pyqt/) / Qt Designer
- **Base de Dados:** [MySQL](https://www.mysql.com/)
- **Conector de Dados:** [PyMySQL](https://github.com/PyMySQL/PyMySQL)

---

## 📂 Estrutura do Projeto

```text
├── formularioQT/
│   ├── controle.py          # Lógica principal da aplicação e conexão à base de dados
│   ├── formulario.ui        # Interface gráfica do ecrã de registo
│   └── listar_dados.ui      # Interface gráfica do ecrã de listagem e remoção
├── mysqlworkbench.mwb       # Modelo da base de dados no MySQL Workbench
└── README.md
