# Arquivo de constantes e configurações da aplicação
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_PROJETO = os.path.join(BASE_DIR, "data", "projetos.json")
ARQUIVO_TAREFAS = os.path.join(BASE_DIR, "data", "tarefas.json")

dict_projetos = {}
dict_tarefas = {}

projeto_ativo = ""
