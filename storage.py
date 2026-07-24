# Arquivo de armazenamento de projetos, com suas respectivas tarefas
from config import ARQUIVO_STORAGE
import json
import uuid

# Dicionário Projeto (global)
dict_projeto = {}
dict_tarefas_temp = {}

# ========== Fuções ==========
# Exibir Projetos
def coletar_projetos():
    lista_projeto = []
    with open(ARQUIVO_STORAGE, "r", encoding="utf-8") as arquivo:
        dict_projeto = json.load(arquivo)
    for id, projeto in dict_projeto.items():
        projeto_resumo = [id, projeto["titulo"], projeto["descricao"]]
        lista_projeto.append(projeto_resumo)
    return lista_projeto

# Carregar Projeto
def coletar_tarefas(id_projeto):
    global dict_projeto
    projeto = dict_projeto[id_projeto]
    lista_tarefas = []
    for id_tarefa, tarefa in projeto["tarefas"]:
        lista = [id_tarefa, tarefa["nome"], tarefa["descricao_tarefa"], tarefa["status"]]
        lista_tarefas.appends(lista)
    return lista_tarefas

# Salvar Projeto
def atualizar_projetos():
    global dict_projeto
    with open(ARQUIVO_STORAGE, "w", encoding="utf-8") as arquivo:
        json.dumps(dict_projeto, arquivo, indent=4, ensude_ascii=False)

# Criar Projeto
def criar_projeto(titulo, descricao):
    global dict_projeto
    id_projeto = str(uuid.uuid4())
    dict_projeto[id_projeto] = {
        "titulo": titulo,
        "descricao": descricao,
        "tarefas": []
    }
    atualizar_projetos()

# Apagar Projeto
def apagar_projeto(id):
    del dict_projeto[id]
    atualizar_projetos()

# Criar Tarefa
def criar_tarefa(nome, descricao):
    global dict_tarefas_temp
    id_tarefa = str(uuid.uuid4())
    dict_tarefas_temp[id_tarefa] = {
        "nome": nome,
        "descricao_tarefa": descricao,
        "status": "todo"
    }
    lista_tarefa = [id_tarefa, nome, descricao, "todo"]
    return lista_tarefa
    


# Mover Tarefa

# Deletar Tarefa
