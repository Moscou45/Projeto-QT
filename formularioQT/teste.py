import sys
import subprocess

try:
    import pymysql
    print("Sucesso! PyMySQL está instalado.")
except ImportError:
    print("PyMySQL NÃO encontrado. Tentando instalar agora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymysql"])
    print("Instalação concluída. Tente rodar seu código principal agora.")
    

    